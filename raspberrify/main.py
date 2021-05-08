import pprint
import requests
import raspberrify.spotify as spotify
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

    spotify.get_cover(sp).show()


if __name__ == "__main__":
    main()
