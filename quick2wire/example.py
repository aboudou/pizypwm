#!/usr/bin/python
import time
import signal

from pizypwm import *

# Called on process interruption. Set all pins to "Input" default mode.
def endProcess(signalnum = None, handler = None):
    first.stop()
    second.stop()
    third.stop()
    fourth.stop()
    fifth.stop()
    sixth.stop()
    seventh.stop()
    eighth.stop()
    exit(0)

# Prepare handlers for process exit
signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)

# Initialize PWM outputs
first   = PiZyPwm(100, 0)
second  = PiZyPwm(100, 1)
third   = PiZyPwm(100, 2)
fourth  = PiZyPwm(100, 3)
fifth   = PiZyPwm(100, 4)
sixth   = PiZyPwm(100, 5)
seventh = PiZyPwm(100, 6)
eighth  = PiZyPwm(100, 7)

# Initialize directions 
#  "up" = we will allocate more and more time to HIGH output (aka the LED will be brighter)
#  "down" = we will allocate less and less time to HIGH output (aka the LED will be dimmer)
directions = ["up", "up", "up", "up", "up", "up", "up", "up"]

# Initialize the starting duty cycle
duties = [0, 14, 28, 42, 56, 70, 84, 100]
#duties = [0, 0, 0, 0, 0, 0, 0, 0]

# Start PWM output
first.start(duties[0])
second.start(duties[1])
third.start(duties[2])
fourth.start(duties[3])
fifth.start(duties[4])
sixth.start(duties[5])
seventh.start(duties[6])
eighth.start(duties[7])

while True:

  # Change duty cycle
  first.changeDutyCycle(duties[0])
  second.changeDutyCycle(duties[1])
  third.changeDutyCycle(duties[2])
  fourth.changeDutyCycle(duties[3])
  fifth.changeDutyCycle(duties[4])
  sixth.changeDutyCycle(duties[5])
  seventh.changeDutyCycle(duties[6])
  eighth.changeDutyCycle(duties[7])
  time.sleep(0.01)

  i = 0
  while i < len(duties): 
    if duties[i] == 100:
      directions[i]="down"
    if duties[i] == 0:
      directions[i]="up"
    i += 1

  i = 0
  while i < len(directions):
    if directions[i] == "up":
      duties[i] += 1
    if directions[i] == "down":
      duties[i] -= 1
    i += 1

