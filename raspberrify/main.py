import pprint
import requests
import raspberrify.spotify as spotify
from dotenv import dotenv_values

def main() -> None:

    config = dotenv_values("../.env.secrets")
    for key, value in config.items():
        print(key, value)

if __name__ == "__main__":
    main()
