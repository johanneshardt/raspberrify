import raspberrify.spotify as spotify
import raspberrify.sense as sense
import threading
from time import sleep
from PIL import Image
from dotenv import dotenv_values

# Time to wait between fetching information from the spotify api
SPOTIFY_REFRESH_DELAY = 3


def main() -> None:

    config = dotenv_values("../.env.secrets")

    """for key, value in config.items():
        print(f"{key}: {value}")"""

    sp = spotify.authorize(
        client_id=config["CLIENT_ID"],
        client_secret=config["CLIENT_SECRET"],
        redirect_uri=config["REDIRECT_URI"],
    )

    print("Authorization succeeded!")
    player = spotify.Playback(sp=sp)
    print("Initialized")
    cached_track = None

    while True:
        player.refresh()
        if cached_track != player.track_id:
            im = player.get_cover().resize(size=(8, 8), resample=Image.LANCZOS)
            sense.show(list(im.getdata()))

        cached_track = player.track_id
        sleep(SPOTIFY_REFRESH_DELAY)


if __name__ == "__main__":
    main()
