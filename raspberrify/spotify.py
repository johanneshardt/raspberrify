import spotipy
import requests
import threading, logging
from PIL import Image
from spotipy.oauth2 import SpotifyOAuth
from enum import Enum, unique, auto

logger = logging.getLogger(__name__)


@unique
class State(Enum):
    PLAYING = auto()
    PAUSED = auto()


class Playback:
    def __init__(self, sp: spotipy.client.Spotify, lock: threading.Lock):
        self.client = sp
        self.lock = lock
        self.track = None
        self.track_id = None
        self.state = None
        self.volume = None
        self.image_link = None
        self.cached_track = None
        self.refresh()

    def refresh(self) -> None:
        self.lock.acquire()
        p = self.client.current_playback()

        if p is not None and p["item"] is not None:
            self.state = State.PLAYING if p["is_playing"] else State.PAUSED
            self.track = p["item"]["name"]
            self.track_id = p["item"]["id"]
            self.image_link = p["item"]["album"]["images"][0]["url"]
            self.volume = p["device"]["volume_percent"]
        else:
            self.status = State.PAUSED
        self.lock.release()

    def get_cover(self) -> Image.Image:
        response = requests.get(self.image_link, stream=True)
        response.raise_for_status()
        im = Image.open(response.raw)
        return im

    def toggle_playback(self) -> None:
        self.refresh()
        self.lock.acquire()  # TODO improve

        if self.state == State.PLAYING:
            self.client.pause_playback()
            self.state = State.PAUSED
            logger.info(msg=f"Paused playback.")
        else:
            self.client.start_playback()
            self.state = State.PLAYING
            logger.info(msg="Resumed playback.")
        # TODO Handle case when nothing is playing??
        self.lock.release()

    def next(self) -> None:
        self.lock.acquire()
        self.client.next_track()
        self.lock.release()

    def previous(self) -> None:
        self.lock.acquire()
        self.client.previous_track()
        self.lock.release()

    def modify_volume(self, step: int) -> None:
        self.lock.acquire()
        new_volume = min(100, max(0, self.volume + step))
        self.client.volume(new_volume)
        self.volume = new_volume
        logger.info(msg=f"Set volume to {new_volume}.")
        self.lock.release()


# TODO combine with Playback class somehow?
def authorize(
    client_id: str, client_secret: str, redirect_uri: str
) -> spotipy.client.Spotify:
    scope = [
        "user-read-currently-playing",
        "user-library-read",
        "user-read-playback-state",
        "streaming",
        "user-modify-playback-state",
    ]
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=" ".join(scope),
        )
    )

    return sp
