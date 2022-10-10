import droid
import asyncio
from time import sleep
from random import randrange


lastSound = -1
async def play_sound(d):
    # number = input("Please input a number of which sound to play. ")
    global lastSound
    sound = lastSound
    while sound == lastSound:
        sound = randrange(0,5)
    lastSound = sound
    await d.play_sound(f"0{sound}","00")

runningDroid = True

async def quit(d):
    global runningDroid
    runningDroid = False

async def main():
    # first, get droid
    d = await droid.discoverDroid(retry=True)

    commands = {
            #"w":forward,
            #"a": left,
            #"s": backward,
            #"d": right,
            #"e": rotate counter-clockwise,
            #"r": rotate clockwise,
            #"f": special effect
            "n":play_sound,
            "q":quit
            }
    try:
        await d.connect()
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
        await d.disconnect()

if __name__ == "__main__":
    asyncio.run(main())