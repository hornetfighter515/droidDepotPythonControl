import droid_commands as d
import asyncio
from time import sleep

import lgpio as GPIO

NOISE = 16


todo = []


def play_sound(handle, gpio, edge, time):
    print(f"Playing sound at {time}")
    todo.append(d.play_sound())


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
    GPIO.gpio_set_debounce_micros(pi, NOISE, 200)
    print("Configuring callback")
    loop = asyncio.get_running_loop()
    cb = GPIO.callback(pi, NOISE, func=play_sound)
    print("Callback configured")
    await droid_connect(pi)




if __name__ == "__main__":
    asyncio.run(main())