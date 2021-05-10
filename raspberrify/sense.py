from sense_hat import SenseHat
from typing import List

sense = SenseHat()
sense.set_rotation(r=180)
sense.clear()


def show(matrix: List[List[int]]) -> None:
    print("hi")
    if len(matrix) == 64 and all(len(e) == 3 for e in matrix):
        sense.set_pixels(matrix)
    else:
        print("Invalid matrix dimensions")


