# raspberrify
A minimal Spotify interface for the Raspberry Pi SenseHat.

## Description
The [Raspberry Pi SenseHat](https://www.raspberrypi.org/products/sense-hat/) has an 8x8 LED matrix as well as a small joystick. Using the [Spotify Web API](https://developer.spotify.com/documentation/web-api/), it's possible to fetch album art to display on the SenseHat matrix, as well as control playback using the joystick. These are the features targeted for an 1.0.0 release.

## Getting started
### Installation
This project is using [Poetry](https://python-poetry.org/) for dependence management. After installing Poetry, run ```poetry install``` in the root directory to download all dependencies.

### Configuration
Secrets needed for [Spotify authorization](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app) are specified in ```.env``` files. The provided ```.env.example``` shows the requred fields. Create a ```.env.secrets``` file to specify your credentials, which can be obtained through the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

## Version history

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements
* [Dotenv](https://pypi.org/project/python-dotenv/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Poetry](https://python-poetry.org/)
* [Requests](https://docs.python-requests.org/en/master/)
* [Spotipy](https://spotipy.readthedocs.io/en/2.18.0/#authorization-code-flow)
* [README template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)

