from enum import Enum, unique
import logging, functools
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED, InputEvent
from typing import List, Callable

logger = logging.getLogger(__name__)

SENSE = SenseHat()
SENSE.set_rotation(r=180)
SENSE.clear()


@unique
class Trigger(Enum):
    PRESS = ACTION_PRESSED
    HOLD = ACTION_HELD
    RELEASE = ACTION_RELEASED


def show(matrix: List[List[int]]) -> None:
    if len(matrix) == 64 and all(len(e) == 3 for e in matrix):
        SENSE.set_pixels(matrix)
    else:
        logger.exception(msg="Invalid matrix dimensions.")


def link_stick(
    on_up: tuple[Callable, list[Trigger]],
    on_down: tuple[Callable, list[Trigger]],
    on_left: tuple[Callable, list[Trigger]],
    on_right: tuple[Callable, list[Trigger]],
    on_middle: tuple[Callable, list[Trigger]],
    on_all: tuple[Callable, list[Trigger]] = None,
) -> None:

    def conditional(func, triggers: list[Trigger]):
        @functools.wraps(func)
        def wrapper(event: InputEvent):
            if event.action in [t.value for t in triggers]:
                return func()

        return wrapper

    SENSE.stick.direction_up = conditional(*on_up)
    SENSE.stick.direction_down = conditional(*on_down)
    SENSE.stick.direction_left = conditional(*on_left)
    SENSE.stick.direction_right = conditional(*on_right)
    SENSE.stick.direction_middle = conditional(*on_middle)

    if on_all is not None:
        SENSE.stick.direction_any = conditional(*on_all)

