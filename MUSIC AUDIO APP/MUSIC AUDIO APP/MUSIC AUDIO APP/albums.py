# albums.py
import requests
from PIL import Image
from io import BytesIO

API_KEY = 2
TADB_ARTIST_ID = 112024 
AUDIO_DB_ALBUMS_URL = f"https://www.theaudiodb.com/api/v1/json/{API_KEY}/album.php?i={TADB_ARTIST_ID}"

def fetch_albums_from_api():
    """
    Fetch album data for the given artist from TheAudioDB.
    Returns a list of albums or an empty list if there is an error.
    """
    try:
        resp = requests.get(AUDIO_DB_ALBUMS_URL, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return data.get("album", [])
    except requests.RequestException as e:
        print("Error fetching albums:", e)
        return []