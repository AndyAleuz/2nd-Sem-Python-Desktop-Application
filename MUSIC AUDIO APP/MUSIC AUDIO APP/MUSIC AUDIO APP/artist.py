# artist.py

import requests
from PIL import Image
from io import BytesIO

API_KEY = 2
TADB_ARTIST_ID = 112024
AUDIO_DB_ARTIST_URL = f"https://www.theaudiodb.com/api/v1/json/{API_KEY}/artist.php?i={TADB_ARTIST_ID}"

def fetch_artist_from_api():
    """
    Fetch artist data from TheAudioDB.
    Returns artist details or an empty list if there is an error.
    """
    try:
        resp = requests.get(AUDIO_DB_ARTIST_URL, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return data.get("artist", [])
    except requests.RequestException as e:
        print("Error fetching artist:", e)
        return []