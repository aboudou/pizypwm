#!/usr/bin/python
import RPi.GPIO as GPIO
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

    GPIO.cleanup()
    exit(0)

# Prepare handlers for process exit
signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)

# Initialize PWM outputs
first   = PiZyPwm(0.01, 100, 7, GPIO.BOARD)
second  = PiZyPwm(0.01, 100, 11, GPIO.BOARD)
third   = PiZyPwm(0.01, 100, 12, GPIO.BOARD)
fourth  = PiZyPwm(0.01, 100, 13, GPIO.BOARD)
fifth   = PiZyPwm(0.01, 100, 15, GPIO.BOARD)
sixth   = PiZyPwm(0.01, 100, 16, GPIO.BOARD)
seventh = PiZyPwm(0.01, 100, 18, GPIO.BOARD)
eighth  = PiZyPwm(0.01, 100, 22, GPIO.BOARD)

# Initialize directions 
#  "up" = we will allocate more and more time to HIGH output (aka the LED will be brighter)
#  "down" = we will allocate less and less time to HIGH output (aka the LED will be dimmer)
directions = ["up", "up", "up", "up", "up", "up", "up", "up"]

# Initialize the starting number of slices of HIGH output
slices = [0, 14, 28, 42, 56, 70, 84, 100]
#slices = [0, 0, 0, 0, 0, 0, 0, 0]

# Start PWM output
first.start(slices[0])
second.start(slices[1])
third.start(slices[2])
fourth.start(slices[3])
fifth.start(slices[4])
sixth.start(slices[5])
seventh.start(slices[6])
eighth.start(slices[7])

while True:

  # Change number of slices of HIGH output
  first.changeNbSlicesOn(slices[0])
  second.changeNbSlicesOn(slices[1])
  third.changeNbSlicesOn(slices[2])
  fourth.changeNbSlicesOn(slices[3])
  fifth.changeNbSlicesOn(slices[4])
  sixth.changeNbSlicesOn(slices[5])
  seventh.changeNbSlicesOn(slices[6])
  eighth.changeNbSlicesOn(slices[7])
  time.sleep(0.01)

  i = 0
  while i < len(slices): 
    if slices[i] == 100:
      directions[i]="down"
    if slices[i] == 0:
      directions[i]="up"
    i += 1

  i = 0
  while i < len(directions):
    if directions[i] == "up":
      slices[i] += 1
    if directions[i] == "down":
      slices[i] -= 1
    i += 1

