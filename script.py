import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotdl import Spotdl
from dotenv import load_dotenv
from helper import *
import dataclasses


def get_playlist_from_id(sp: spotipy.Spotify, id: str) -> Playlist:
    object = dict(sp.playlist(id))
    return JSONSpotifyConverter.toPlaylist(object)


def initialise_spotipy():
    load_dotenv()
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    return spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    )


def main():
    sp = initialise_spotipy()
    playlist = get_playlist_from_id(sp, '1VRQ7AA8N9jRc3yP9UOzGQ')


if __name__ == "__main__":
    main()