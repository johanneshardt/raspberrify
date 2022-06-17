import logging
from sense_hat import SenseHat
from typing import List, Callable

logger = logging.getLogger(__name__)

SENSE = SenseHat()
SENSE.set_rotation(r=180)
SENSE.clear()


def show(matrix: List[List[int]]) -> None:
    if len(matrix) == 64 and all(len(e) == 3 for e in matrix):
        SENSE.set_pixels(matrix)
    else:
        logger.exception(msg="Invalid matrix dimensions.")


def link_stick(
    on_up: Callable,
    on_down: Callable,
    on_left: Callable,
    on_right: Callable,
    on_middle: Callable,
    on_all: Callable = None,
) -> None:
    SENSE.stick.direction_up = on_up
    SENSE.stick.direction_down = on_down
    SENSE.stick.direction_left = on_left
    SENSE.stick.direction_right = on_right
    SENSE.stick.direction_middle = on_middle

    if on_all is not None:
        SENSE.stick.direction_any = on_all
