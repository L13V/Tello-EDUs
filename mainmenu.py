import signal
import time
import readchar
import socket
import sys
import termcolor
from termcolor import colored, cprint
import threading

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Drone Initial Setup Function
def droneinit():

    print('Starting Drone SDK')
    sock1.sendto('command'.encode(), 0, ('192.168.8.101', 8889))
    sock2.sendto('command'.encode(), 0, ('192.168.8.102', 8889))
    sock3.sendto('command'.encode(), 0, ('192.168.8.103', 8889))
# Main Menu
def handler(signum, frame):

    msg = " \n -------------------------------- \nDrones Paused \nMain Menu:\n1. Land All Drones \n2. Land Specific Drone \n3. EMERGENCY LAND ALL \n4. EMERGENCY LAND SPECIFIC DRONE \n5. Exit \nPress any other button to resume/ Close Menu"
    print(msg, end="", flush=True)
    resmenu = readchar.readchar()
#All Drone Landing

    if resmenu == '1':
        print('\nYou Pressed Number one!')
        termcolor.cprint('Landing all drones', 'yellow')
        droneinit()
        sock1.sendto('land'.encode(), 0, ('192.168.8.101', 8889))
        sock2.sendto('land'.encode(), 0, ('192.168.8.102', 8889))
        sock3.sendto('land'.encode(), 0, ('192.168.8.103', 8889))
        print('Closing')
        exit(0)
#Specific drone landing

    elif resmenu == '2':
        print('What drone would you like to land?')
        print('1, 2, or 3')
        time.sleep(0.01)
        res2 = readchar.readchar()
#Select 1 2 or 3 (the drone to land)

        if resmenu == '1':
            droneinit()
            sock1.sendto('land'.encode(), 0, ('192.168.8.101', 8889))
            termcolor.cprint('Resuming Show', 'yellow')
        elif resmenu == '2':
            droneinit()
            sock2.sendto('land'.encode(), 0, ('192.168.8.102', 8889))
            termcolor.cprint('Resuming Show', 'yellow')
        elif resmenu == '3':
            droneinit()
            sock3.sendto('land'.encode(), 0, ('192.168.8.103', 8889))
            termcolor.cprint('Resuming Show', 'yellow')
        else:
            print('Incorrect Number Pressed \nLeaving Page')
#EMERGENCY drop all drones1

    elif resmenu == '3':
        termcolor.cprint('EMERGENCY DROP INITIATED \n be Careful! \n Initializing Low Latency Control', 'red')
        droneinit()
        print('Done')
        termcolor.cprint('Dropping Drones NOW!', 'red')
        sock1.sendto('emergency'.encode(), 0, ('192.168.8.101', 8889))
        sock2.sendto('emergency'.encode(), 0, ('192.168.8.102', 8889))
        sock3.sendto('emergency'.encode(), 0, ('192.168.8.103', 8889))
        print('Closing')
        exit(0)
#Select Emergency drop drone
    elif resmenu == '4':
        print('EMERGENCY DROP INITIATED THIS WILL DROP ONE DRONE')
        print('1, 2, or 3?')
        print('Pressing any other letter will drop ALL drones!')
        time.sleep(0.1)
        res4 = readchar.readchar()
        if res4 == '1':
            termcolor.cprint('EMERGENCY DROP INITIATED \n be Careful! \n Initializing Low Latency Control', 'red')
            droneinit()
            print('Done')
            print('Dropping Drones NOW!')
            sock1.sendto('emergency'.encode(), 0, ('192.168.8.101', 8889))
            print('Drone Dropped')
            print('Resuming Show')
        elif res4 == '2':
            termcolor.cprint('EMERGENCY DROP INITIATED \n be Careful! \n Initializing Low Latency Control', 'red')
            droneinit()
            print('Done')
            print('Dropping Drones NOW!')
            sock2.sendto('emergency'.encode(), 0, ('192.168.8.102', 8889))
            print('Drone Dropped')
            print('Resuming Show')
        elif res4 == '3':
            termcolor.cprint('EMERGENCY DROP INITIATED \n be Careful! \n Initializing Low Latency Control', 'red')
            droneinit()
            print('Done')
            print('Dropping Drones NOW!')
            sock3.sendto('emergency'.encode(), 0, ('192.168.8.103', 8889))
            print('Drone Dropped')
            print('Resuming Show')
        else:
            termcolor.cprint('Incorrect Number Pressed \nDROPPING ALL DRONES\nSTEER CLEAR FROM DRONES!')
            print('Dropping Drones NOW!')
            sock1.sendto('emergency'.encode(), 0, ('192.168.8.101', 8889))
            sock2.sendto('emergency'.encode(), 0, ('192.168.8.102', 8889))
            sock3.sendto('emergency'.encode(), 0, ('192.168.8.103', 8889))
            print('Drones Dropped')
            print('Sorry if you did this on accident :(')
            print('Closing File')
            exit(0)
#Menu Close
    else:
        print('Menu Closing...')
        print("", end="", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)
def start():
    termcolor.cprint('''
    /$$       /$$                      /$$              /$$$$$$$$        /$$ /$$                 /$$$$$$$$                  /$$
    | $$      |__/                     | $/             |__  $$__/       | $$| $$                |__  $$__/                 | $$
    | $$       /$$  /$$$$$$  /$$    /$$|_//$$$$$$$         | $$  /$$$$$$ | $$| $$  /$$$$$$          | $$  /$$$$$$   /$$$$$$ | $$
    | $$      | $$ /$$__  $$|  $$  /$$/  /$$_____/         | $$ /$$__  $$| $$| $$ /$$__  $$         | $$ /$$__  $$ /$$__  $$| $$
    | $$      | $$| $$$$$$$$ \  $$/$$/  |  $$$$$$          | $$| $$$$$$$$| $$| $$| $$  \ $$         | $$| $$  \ $$| $$  \ $$| $$
    | $$      | $$| $$_____/  \  $$$/    \____  $$         | $$| $$_____/| $$| $$| $$  | $$         | $$| $$  | $$| $$  | $$| $$
    | $$$$$$$$| $$|  $$$$$$$   \  $/     /$$$$$$$/         | $$|  $$$$$$$| $$| $$|  $$$$$$/         | $$|  $$$$$$/|  $$$$$$/| $$
    |________/|__/ \_______/    \_/     |_______/          |__/ \_______/|__/|__/ \______/          |__/ \______/  \______/ |__/




    ''','green')

    signal.signal(signal.SIGINT, handler)

    print('''Welcome to Liev's Tello Tool''')
    termcolor.cprint('Press one to run the show!', 'cyan')
    termcolor.cprint('Press two to run the liftoff tester', 'yellow')
    termcolor.cprint('Press three to close the utility', 'red')
    resopen = readchar.readchar()
    if resopen == '1':
        while True:
            print('Running Show')
            import alltellos
    if resopen == '2':
        while True:
            import liftoff
    if resopen == '3':
        print('Closing')
        time.sleep(0.5)
        exit(0)
start()
