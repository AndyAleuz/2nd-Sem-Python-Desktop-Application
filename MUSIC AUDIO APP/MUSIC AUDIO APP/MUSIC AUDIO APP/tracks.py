# tracks.py name of the module

import requests
from PIL import Image
from io import BytesIO

API_KEY = 2
TADB_ALBUM_ID = 2115888
AUDIO_DB_TRACKS_URL = f"https://www.theaudiodb.com/api/v1/json/{API_KEY}/track.php?m={TADB_ALBUM_ID}"

def fetch_tracks_from_api():
    """
    Fetch track data for the given album from TheAudioDB.
    Returns a list of tracks or an empty list if there is an error.
    """
    try:
        resp = requests.get(AUDIO_DB_TRACKS_URL, timeout=2)
        resp.raise_for_status()
        data = resp.json()
        return data.get("track", [])
    except requests.RequestException as e:
        print("Error fetching tracks:", e)
        return []