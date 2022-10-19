import droid
import asyncio
from time import sleep
from random import randrange

d = ""


lastSound = -1
async def play_sound():
    # number = input("Please input a number of which sound to play. ")
    global lastSound
    global d
    sound = lastSound
    while sound == lastSound:
        sound = randrange(0,5)
    lastSound = sound

    while d is None:
        sleep(0.1)

    await d.play_sound(f"0{sound}","00")


async def play_specific_sound(bank, sound):
    await d.play_sound( sound_id = sound, bank_id = bank)


async def move_droid(direction):
    global d
    await d.move_motors(droid.Directions.FORWARD, droid.Motors.LEFT, "FF")
    await d.move_motors(droid.Directions.FORWARD, droid.Motors.RIGHT,"FF")


async def stop_droid():
    await d.move_motors(droid.Directions.FORWARD, droid.Motors.LEFT, "00")
    await d.move_motors(droid.Directions.FORWARD, droid.Motors.RIGHT, "00")



async def start_droid():
    """
    This function should be in a try loop
    """
    global d
    d = await droid.discoverDroid(retry=True)
    await d.connect()


async def stop_droid():
    global d
    await d.disconnect()
    