import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotdl import Spotdl
from dotenv import load_dotenv


load_dotenv()
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')


sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
)

print(sp.playlist('1VRQ7AA8N9jRc3yP9UOzGQ'))
