import os
import platform

SYS_PLATFORM = platform.system()
DEVELOPER = 'TanmayXD'

def devInfo():
    return DEVELOPER

def clearScreen():
    if SYS_PLATFORM == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def showOS():
    return SYS_PLATFORM

