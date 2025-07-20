import requests
import json
import os
from tqdm import tqdm

API_KEY = "3f839dcd0063c880932d78d186b74325"
BASE_URL = "https://api.themoviedb.org/3"

OUTPUT_FILE = "data/movies_series_10k.json"
PROGRESS_FILE = "data/progress.json"
PAGES_PER_RUN = 10

def load_existing_data():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_data(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data.get("current_page", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def save_progress(current_page):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump({"current_page": current_page}, f, ensure_ascii=False, indent=2)

def fetch_movies(page):
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def main():
    existing_data = load_existing_data()
    existing_ids = set(entry["id"] for entry in existing_data)

    current_page = load_progress()
    last_page = current_page + PAGES_PER_RUN - 1

    new_entries = []

    for page in tqdm(range(current_page, last_page + 1), desc="Fetching pages"):
        movies = fetch_movies(page)
        for movie in movies:
            movie_id = movie.get("id")
            if movie_id in existing_ids:
                continue

            details = fetch_movie_details(movie_id)
            if not details:
                continue

            entry = {
                "id": details.get("id"),
                "title": details.get("title"),
                "type": "movie",
                "genre": [g["name"] for g in details.get("genres", [])],
                "duration": details.get("runtime", 0)
            }

            new_entries.append(entry)
            existing_ids.add(movie_id)

    if new_entries:
        save_data(existing_data + new_entries)
        print(f"{len(new_entries)} yeni içerik eklendi.")
    else:
        print("Yeni içerik bulunamadı.")

    save_progress(last_page + 1)  # Sonraki çalıştırmada buradan başla

if __name__ == "__main__":
    main()
