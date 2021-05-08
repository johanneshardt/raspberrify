from PIL import Image
import pprint
import requests
import raspberrify.spotify as spotify

def main() -> None:
    sp = spotify.authorize()
    track = sp.currently_playing()
    if track is not None:
        name = track['item']['name']
        image_url = track['item']['album']['images'][0]['url']

        im = Image.open(requests.get(image_url, stream=True).raw)
        pprint.pprint(name)
        im.show()
    else:
        print("No track is currently playing.")


if __name__ == "__main__":
    main()
