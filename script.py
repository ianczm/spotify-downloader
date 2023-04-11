import os
import re
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


def extract_playlist_id(url: str):
    return re.match('.*playlist\/(.*)', url).group(1).partition('?')[0]


def prompt_user_input():
    playlist = input('Enter Spotify playlist link: ')
    output_path = input('Enter output path: ')
    return playlist, output_path


def confirm_choice(playlist: Playlist):
    print(f'About to download playlist: {playlist.name} by {playlist.owner_name}')
    choice = input('Confirm? (y/n) ')
    return choice.lower() == 'y'


def main():
    playlist, output_path = prompt_user_input()

    sp, spotdl = initialise_services(output_path)
    playlist = get_playlist_from_id(sp, extract_playlist_id(playlist))

    if confirm_choice(playlist):
        # print(json.dumps(dataclasses.asdict(playlist), indent=2))
        songs = spotdl.search([track.url for track in playlist.tracks])

        shutil.rmtree(output_path)
        # print(songs)
        spotdl.download_songs(songs)
    else:
        print('Exiting...')


if __name__ == "__main__":
    main()
