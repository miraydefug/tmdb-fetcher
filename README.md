# TMDB Fetcher

This Python project is designed to fetch movie and TV show data from [The Movie Database (TMDB)](https://www.themoviedb.org/) API. It stores the data in a local JSON file and avoids duplication across multiple runs. Additionally, it remembers the last fetched page to continue fetching new content incrementally.

---

## ✨ Features

- Fetches movies and series (TV shows) from TMDB.
- Automatically skips previously saved content.
- Fetches 10 pages of new data each time the script runs.
- Remembers the last fetched page in a progress file.
- Saves output in a structured JSON file.

---

## 📁 Project Structure

tmdb-fetcher/
│
├── fetch_movies.py # Main script
├── data/
│ ├── movies_series_10k.json # Fetched data stored here
│ └── progress.json # Tracks last fetched page
├── requirements.txt # Required Python packages
└── README.md # This file

---

## 🔧 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/tmdb-fetcher.git
cd tmdb-fetcher

---

Install dependencies:
pip install -r requirements.txt

---

Make sure the data folder and JSON files exist:
mkdir -p data
echo "[]" > data/movies_series_10k.json
echo '{"last_page": 0}' > data/progress.json

🚀 How to Run

Run the script using:

python fetch_movies.py
Each time you run it, the script:

Fetches 10 new pages of data
Appends only new items (skips duplicates)
Updates progress.json with the last fetched page
You can open the JSON file in any editor or use it in your own applications.

---

🧪 API Requirement

You must provide your own TMDB API key inside the script. Replace this line in fetch_movies.py:

API_KEY = "YOUR_TMDB_API_KEY"
Get your key from: https://developer.themoviedb.org/

---

