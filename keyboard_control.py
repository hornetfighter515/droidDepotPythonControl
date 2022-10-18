import asyncio
from time import sleep
from random import randrange
import droid_commands as d



runningDroid = True

async def quit(d):
    global runningDroid
    runningDroid = False

async def main():
    # first, get droid
    await d.start_droid()

    commands = {
            #"w":forward,
            #"a": left,
            #"s": backward,
            #"d": right,
            #"e": rotate counter-clockwise,
            #"r": rotate clockwise,
            #"f": special effect
            "n":d.play_sound,
            "q":quit
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
            elif c == "m":
                bank = input("\tBank> ")
                sound = input("\tSound> ")
                await d.play_specific_sound(bank, sound)
            else:
                print("Command does not exist.")


            sleep(0.2)

    finally:
        await d.stop_droid()

if __name__ == "__main__":
    asyncio.run(main())