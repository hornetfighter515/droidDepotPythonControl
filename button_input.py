import droid_commands as d
import asyncio
from time import sleep

import lgpio as GPIO

NOISE = 16

LEFT = 26
DOWN = 27
UP = 25
RIGHT = 19

ROT_LEFT = 6
ROT_RIGHT = 5


todo = []


def play_sound(handle, gpio, edge, time):
    print(f"Playing sound at {time}")
    todo.append(d.play_sound())


def move(handle, gpio, edge, time):
    # first, kill all other movements
    todo.append(d.move_stop())

    # then, check if this was a falling edge
    if edge == 0:
        return

    if gpio == RIGHT:
        print("Pressed right")
    elif gpio == LEFT:
        print("Pressed left")
    elif gpio == UP:
        print("Pressed forward")
    elif gpio == DOWN:
        print("Pressed backward")


def move_head(handle, gpio, edge, time):
    todo.append(d.move_stop())

    if edge == 0:
        return
    
    if gpio == ROT_LEFT:
        print("Rotating left")
    elif gpio == ROT_RIGHT:
        print("Rotating right")



async def droid_connect(pi):
    try:
        await d.start_droid()
        while True:
            if len(todo) > 0:
                await todo[0]
                todo.pop(0)
    except KeyboardInterrupt:
        print("Thanks for using")
    finally:
        GPIO.gpiochip_close(pi)
        await d.stop_droid()


async def main():
    pi = GPIO.gpiochip_open(0)
    if pi < 0:
        return

    GPIO.gpio_claim_alert(pi, NOISE, GPIO.RISING_EDGE)
    GPIO.gpio_claim_alert(pi, UP, GPIO.BOTH_EDGES)
    
    GPIO.gpio_set_debounce_micros(pi, NOISE, 200)

    cbs = []
    print("Configuring callbacks")

    # noise
    cbs.append(GPIO.callback(pi, NOISE, func=play_sound))

    # up
    cbs.append(GPIO.callback(pi, NOISE, func=play_sound))
    print("Callback configured")
    await droid_connect(pi)




if __name__ == "__main__":
    asyncio.run(main())