from raspberrify.sense import link_stick
import spotify as spotify
import sense as sense
import threading, logging
from time import sleep
from PIL import Image
from dotenv import dotenv_values

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s"
)


def loop(player: spotify.Playback, refresh_delay: int = 3) -> None:
    LoopingTimer(
        interval=refresh_delay, function=fetch_display_info, args=[player]
    ).start()


def fetch_display_info(player: spotify.Playback) -> None:
    player.refresh()
    if player.cached_track != player.track_id:
        logging.info(msg=f"Changed track to {player.track_id}")
        im = player.get_cover().resize(size=(8, 8), resample=Image.Resampling.LANCZOS)
        sense.show(list(im.getdata()))

    player.cached_track = player.track_id  # TODO fix race condition


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
    p = spotify.Playback(sp=sp, lock=threading.Lock())
    logging.info("Initialized client!")

    sense.link_stick(
        on_up=lambda *args, **kwargs: p.modify_volume(5),
        on_down=lambda *args, **kwargs: p.modify_volume(-5),
        on_left=lambda *args, **kwargs: p.previous(),
        on_right=lambda *args, **kwargs: p.next(),
        on_middle=lambda *args, **kwargs: p.toggle_playback(),
        on_all=lambda *args, **kwargs: p.refresh(),
    )

    loop(player=p)


# shamelessly stolen from https://stackoverflow.com/questions/12435211/threading-timer-repeat-function-every-n-seconds
class LoopingTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


if __name__ == "__main__":
    main()
