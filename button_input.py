import droid_commands as d
import asyncio
from time import sleep

import lgpio as GPIO

FEATURE = "feature"
NOISE = "noise"
ROTATE_RIGHT = "rotate-right"
ROTATE_LEFT = "rotate-left"
RIGHT = "right"
UP = "up"
DOWN = "down"
LEFT = "left"


pins = {
    4:FEATURE,
    FEATURE:4,
    17:NOISE,
    NOISE:17,
    22:ROTATE_RIGHT,
    ROTATE_RIGHT:22,
    5:ROTATE_LEFT,
    ROTATE_LEFT:5,
    6: RIGHT,
    RIGHT:6,
    23: UP,    
    UP : 23,
    24: DOWN,
    DOWN: 24,
    25: LEFT,
    LEFT:25
}


def play_sound():
    print("Playing sound")
    asyncio.run_coroutine_threadsafe( d.play_sound())


async def main():
    pi = GPIO.gpiochip_open(0)
    GPIO.gpio_claim_input(pi, pins[NOISE])
    GPIO.callback(pi, pins[NOISE], edge=1, func=play_sound)
    try:
        await d.start_droid()
        while True:
            sleep(10)
    finally:
        await d.stop_droid()

        


if __name__ == "__main__":
    asyncio.run(main())
