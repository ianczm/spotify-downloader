import os
import json
import shutil
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotdl import Spotdl
from dotenv import load_dotenv
from helper import *
import dataclasses


def get_playlist_from_id(sp: spotipy.Spotify, id: str) -> Playlist:
    object = dict(sp.playlist(id))
    return JSONSpotifyConverter.toPlaylist(object)


def initialise_services(output_path: str):
    load_dotenv()
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    return spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    ), Spotdl(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        downloader_settings={'output': output_path}
    )


def main():
    output_path = './downloads'
    sp, spotdl = initialise_services(output_path)
    playlist = get_playlist_from_id(sp, '1VRQ7AA8N9jRc3yP9UOzGQ')

    # print(json.dumps(dataclasses.asdict(playlist), indent=2))
    songs = spotdl.search([track.url for track in playlist.tracks])

    shutil.rmtree(output_path)
    # print(songs)    
    spotdl.download_songs(songs)



if __name__ == "__main__":
    main()