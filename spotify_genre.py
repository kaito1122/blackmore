import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from the .env file
load_dotenv()

# Get your Spotify credentials from the environment variables
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

# Set up the Spotify OAuth authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read"))


def get_artist_info(artist_name):
    try:
        # Search for the artist
        result = sp.search(q=artist_name, type="artist", limit=1)
        artists = result.get('artists', {}).get('items', [])

        if not artists:
            print(f"No artist found for: {artist_name}")
            return None

        artist = artists[0]
        artist_info = {
            "name": artist["name"],
            "id": artist["id"],
            "genres": artist["genres"],
            "followers": artist["followers"]["total"],
            "popularity": artist["popularity"],
            "url": artist["external_urls"]["spotify"]
        }

        return artist_info

    except Exception as e:
        print(f"Error fetching artist info for '{artist_name}': {e}")
        return None


def get_album_tracks(album_name, artist_name=None):
    # Search for album
    query = f"album:{album_name}"
    if artist_name:
        query += f" artist:{artist_name}"

    result = sp.search(q=query, type="album", limit=1)
    albums = result.get("albums", {}).get("items", [])

    if not albums:
        print(f"No album found for: {album_name}")
        return []

    album_id = albums[0]["id"]

    # Get tracks in the album
    tracks = sp.album_tracks(album_id)["items"]
    track_names = [track["name"] for track in tracks]

    return track_names

print("Blackmore's Night")
print(get_artist_info("Blackmore\'s Night"))

import requests

API_KEY = os.getenv("LASTFM_CLIENT_ID")
artist = "Blackmore's Night"
tracks = get_album_tracks("Under a Violet Moon")
track_genres = dict()

for track in tracks:
    url = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}&artist={artist}&track={track}&format=json"
    response = requests.get(url).json()

    tags = response.get("track", {}).get("toptags", {}).get("tag", [])
    genre_tags = [tag['name'] for tag in tags]
    track_genres[track] = genre_tags

print(track_genres)

from collections import defaultdict
counter = defaultdict(int)
for v in track_genres.values():
    for s in v:
        counter[s] += 1

print(counter)