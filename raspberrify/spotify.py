import spotipy
import requests
from PIL import Image
from spotipy.oauth2 import SpotifyOAuth
from enum import Enum, unique, auto


@unique
class State(Enum):
    PLAYING = auto()
    PAUSED = auto()


class Playback:
    def __init__(self, sp: spotipy.client.Spotify):
        self.client = sp
        self.track = None
        self.track_id = None
        self.state = None
        self.image_link = None
        self.cached_track = None
        self.refresh()

    def refresh(self) -> None:
        track = self.client.currently_playing()

        if track is not None and track["item"] is not None:
            self.state = State.PLAYING
            self.track = track["item"]["name"]
            self.track_id = track["item"]["id"]
            self.image_link = track["item"]["album"]["images"][0]["url"]
        else:
            self.status = State.PAUSED

    def get_cover(self) -> Image.Image:
        response = requests.get(self.image_link, stream=True)
        response.raise_for_status()
        im = Image.open(response.raw)
        return im

    def toggle_playback(self) -> None:
        if self.state == State.PLAYING:
            print("Paused playback.")
            self.pause_playback()
        else:
            print("Resumed playback.")
            self.start_playback()
        # TODO Handle case when nothing is playing??


# TODO combine with Playback class somehow?
def authorize(
    client_id: str, client_secret: str, redirect_uri: str
) -> spotipy.client.Spotify:
    scope = ["user-read-currently-playing", "user-library-read"]
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=" ".join(scope),
        )
    )

    return sp
