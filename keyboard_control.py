import asyncio
from re import L
from time import sleep
from random import randrange
import droid_commands as d
from droid import Directions



runningDroid = True

async def select_noise(d):
    bank = input("\tBank> ")
    sound = input("\tSound> ")
    await d.play_specific_sound(bank, sound)


async def select_speed(d):
    direction = input("\tDirection> ")
    motor = input("\tMotor> ")
    speed = input("\tSpeed> ")
    await d.move_manually(direction, motor, speed)

async def forward(d):
    await d.move_droid(Directions.FORWARD)

async def backward(d):
    await d.move_droid(Directions.BACKWARD)

async def left(d):
    await d.move_droid(Directions.LEFT)

async def right(d):
    await d.move_droid(Directions.RIGHT)

async def stop_droid(d):
    await d.stop_droid()



async def quit(d):
    global runningDroid
    runningDroid = False

async def main():
    # first, get droid
    await d.start_droid()

    commands = {
            "w": forward,
            "a": left,
            "s": backward,
            "d": right,
            "x": stop_droid,
            "z": select_speed,
            #"e": rotate counter-clockwise,
            #"r": rotate clockwise,
            #"f": special effect
            "n": d.play_sound,
            "m": select_noise,
            "q": quit
            }
    try:
        global runningDroid
        while runningDroid:
            # next, await input
            command = input("Please input a command > ")
            # next, parse that command
            c = command.lower()[0:1]
            if c in commands.keys():
                await commands[c](d)
            else:
                print("Command does not exist.")


            sleep(0.2)

    finally:
        await d.stop_droid()

if __name__ == "__main__":
    asyncio.run(main())