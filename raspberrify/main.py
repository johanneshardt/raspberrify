import raspberrify.spotify as spotify
import raspberrify.sense as sense
import threading, logging
from time import sleep
from PIL import Image
from dotenv import dotenv_values

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s"
)

def fetch_info(player: spotify.Playback, refresh_delay: int = 3) -> None:
    cached_track = None

    while True:
        player.refresh()
        if cached_track != player.track_id:
            logging.info(msg="Changed track.")
            im = player.get_cover().resize(size=(8, 8), resample=Image.LANCZOS)
            sense.show(list(im.getdata()))

        cached_track = player.track_id
        threading.Timer(refresh_delay).start


def main() -> None:

    config = dotenv_values("../.env.secrets")

    """for key, value in config.items():
        print(f"{key}: {value}")"""

    sp = spotify.authorize(
        client_id=config["CLIENT_ID"],
        client_secret=config["CLIENT_SECRET"],
        redirect_uri=config["REDIRECT_URI"],
    )

    logging.info("Authorization succeeded!")
    p = spotify.Playback(sp=sp)
    logging.info("Initialized")
    fetch_info(player=p)



if __name__ == "__main__":
    main()
