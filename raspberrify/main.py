import spotify as spotify
import sense as sense
import threading, logging
from time import sleep
from PIL import Image
from dotenv import dotenv_values

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s"
)


def run(player: spotify.Playback, refresh_delay: int = 3) -> None:
    while True:
        threading.Timer(interval=refresh_delay, function=fetch_info(player)).start()


def fetch_info(player: spotify.Playback) -> None:
    player.refresh()
    if player.cached_track != player.track_id:
        logging.info(msg=f"Changed track to {player.track_id}")
        im = player.get_cover().resize(size=(8, 8), resample=Image.LANCZOS)
        sense.show(list(im.getdata()))

    player.cached_track = player.track_id


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
    run(player=p)


if __name__ == "__main__":
    main()
