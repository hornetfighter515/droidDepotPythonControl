import droid
import asyncio
from time import sleep
from random import randrange

d = ""


lastSound = -1
async def play_sound():
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
    global d
    await d.play_sound( sound_id = sound, bank_id = bank)



async def move_droid(forward=False, backward=False, left=False, right=False):

    l = droid.Directions.FORWARD
    r = droid.Directions.FORWARD
    global d


    if forward:
        l = droid.Directions.FORWARD
        r = droid.Directions.FORWARD
    if backward:
        l = droid.Directions.BACKWARD
        r = droid.Directions.BACKWARD
    if left:
        # spin left
        l = droid.Directions.BACKWARD
        r = droid.Directions.FORWARD
    if right:
        # spin right
        l = droid.Directions.FORWARD
        r = droid.Directions.BACKWARD

    await d.move_motors(l, droid.Motors.LEFT, "FF")
    await d.move_motors(r, droid.Motors.RIGHT,"FF")


async def move_manually(direction, motor, strength):
    global d
    await d.move_motors(direction, motor, strength)


async def move_stop():
    global d
    await move_manually(droid.Directions.FORWARD, droid.Motors.LEFT, "00")
    await move_manually(droid.Directions.FORWARD, droid.Motors.RIGHT, "00")


async def rotate_head(direction):
    global d
    await d.move_motors(direction, droid.Motors.HEAD, "FF")
    # eventually should we stop this call so we don't waste a bunch of battery?

async def stop_rotate_head():
    global d
    await d.move_motors(droid.Directions.ROTATE_LEFT, droid.Motors.HEAD, "00")


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
    