import os
import platform

SYS_PLATFORM = platform.system()

def clearScreen():
    if SYS_PLATFORM == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
clearScreen()