from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(r="180")


def show(matrix: list[list[int]]) -> None:

    if len(matrix) == 64 and all(len(e) == 3 for e in matrix):
        sense.set_pixels(matrix)
    else:
        print("Invalid matrix dimensions")
