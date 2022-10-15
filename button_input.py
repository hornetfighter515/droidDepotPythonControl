import droid_commands as d
import asyncio

import RPi.GPIO as GPIO

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
    27:NOISE,
    NOISE:27,
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
    asyncio.run(d.play_sound())


def main():
    # GPIO.setup(pins[FEATURE], GPIO.IN)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins[NOISE], GPIO.IN)
    GPIO.add_event_detect(pins[NOISE], GPIO.RISING, callback=play_sound)
    try:
        asyncio.run( d.start_droid())
    finally:
        asyncio.run( d.stop_droid())

        


if __name__ == "__main__":
    main()
