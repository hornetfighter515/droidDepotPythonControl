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


async def main():
    # GPIO.setup(pins[FEATURE], GPIO.IN)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins[NOISE], GPIO.IN)
    try:
        await d.start_droid()
        GPIO.add_event_detect(pins[NOISE], GPIO.RISING, callback=d.play_sound)
    finally:
        await d.stop_droid()

        


if __name__ == "__main__":
    asyncio.run(main())
