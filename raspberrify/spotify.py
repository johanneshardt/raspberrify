import spotipy
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
