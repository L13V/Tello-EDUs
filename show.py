# This example script demonstrates how to use Python to fly Tello in a box mission
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import sys
import termcolor
from termcolor import colored, cprint
import socket
import threading
import time

termcolor.cprint('Setting variables...', 'yellow')

# IP and port of Tello
tello1_address = ('192.168.8.101', 8889)
tello2_address = ('192.168.8.102', 8889)
tello3_address = ('192.168.8.103', 8889)

# IP and port of local computer
local1_address = ('', 1009)
local2_address = ('', 1010)
local3_address = ('', 1011)

# Create a UDP connection that we'll send the command to
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock1.bind(local1_address)
sock2.bind(local2_address)
sock3.bind(local3_address)

time.sleep(1)
termcolor.cprint('Done!', 'green')

termcolor.cprint('Housekeeping...', 'yellow')

# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock1.sendto(message.encode(), tello1_address)
    sock2.sendto(message.encode(), tello2_address)
    sock3.sendto(message.encode(), tello3_address)
    termcolor.cprint("Sending message: " + message, 'yellow')
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

def sendto1(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock1.sendto(message.encode(), tello1_address)
    termcolor.cprint("Sending message to tello 3: " + message, 'yellow')
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

def sendto2(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock2.sendto(message.encode(), tello2_address)
    termcolor.cprint("Sending message to tello 2: " + message, 'yellow')
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

def sendto3(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock3.sendto(message.encode(), tello3_address)
    termcolor.cprint("Sending message to tello 3: " + message, 'yellow')
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)



# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response1, ip_address = sock1.recvfrom(128)
      response2, ip_address = sock2.recvfrom(128)
      response3, ip_address = sock3.recvfrom(128)

      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #3: " + response3.decode(encoding='utf-8'))

    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock1.close()
      sock2.close()
      sock3.close()
      print("Error receivied: Killing connections" + str(e))
      break

termcolor.cprint('Done!', 'green')

termcolor.cprint('Almost done...', 'yellow')
time.sleep(2)
# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
termcolor.cprint('Start!', 'green')

receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Put Tello into command mode
send("command", 3)

termcolor.cprint('Wating For Takeoff', 'yellow')

# Send the takeoff command
send("takeoff", 5)

send("forward 20", 6)

send("land", 5)

# Print message
termcolor.cprint('Mission Complete!!', 'cyan')

# Close the socket
termcolor.cprint('Closing...', 'yellow')
time.sleep(1)
quit()
