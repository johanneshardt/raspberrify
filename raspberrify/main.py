import pprint
import requests
import raspberrify.spotify as spotify
import raspberrify.sense as sense
from PIL import Image
from dotenv import dotenv_values


def main() -> None:

    config = dotenv_values("../.env.secrets")

    """for key, value in config.items():
        print(f"{key}: {value}")"""

    sp = spotify.authorize(
        client_id=config["CLIENT_ID"],
        client_secret=config["CLIENT_SECRET"],
        redirect_uri=config["REDIRECT_URI"],
    )

    im = spotify.get_cover(sp).resize(size=(8, 8), resample=Image.LANCZOS)
    sense.show(list(im.getdata()))
    print(im.mode)


if __name__ == "__main__":
    main()
