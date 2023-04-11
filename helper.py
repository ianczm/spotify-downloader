from dataclasses import dataclass


class JSONSpotifyConverter:
    @staticmethod
    def toPlaylist(o: dict):
        return Playlist(
            id = o.get('id'),
            uri = o.get('uri'),
            url = o.get('external_urls').get('spotify'),
            owner_name = o.get('owner').get('display_name'),
            owner_id = o.get('owner').get('id'),
            tracks = [JSONSpotifyConverter.toTrack(item) for item in o.get('tracks').get('items')]
        )
    
    @staticmethod
    def toTrack(o: dict):
        trackObj = o.get('track')
        return Track(
            id = trackObj.get('id'),
            url = trackObj.get('external_urls').get('spotify'),
            uri = trackObj.get('uri'),
            name = trackObj.get('name'),
            artist = [artist.get('name') for artist in trackObj.get('artists')]
        )


@dataclass
class Track:
    id: str
    uri: str
    url: str
    name: str
    artist: list[str]


@dataclass
class Playlist:
    id: str
    uri: str
    url: str
    owner_name: str
    owner_id: str
    tracks: list[Track]

