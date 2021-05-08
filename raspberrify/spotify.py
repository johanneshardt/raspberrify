import spotipy
import requests
from PIL import Image
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


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


def get_cover(sp: spotipy.client.Spotify) -> Image.Image:
    track = sp.currently_playing

    if track is not None:
        image_url = track["item"]["album"]["images"][0]["url"]
        im = Image.open(requests.get(image_url, stream=True).raw)
        return im
    else:
        print("No track is currently playing.")
