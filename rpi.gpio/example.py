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
first   = PiZyPwm(100, 7, GPIO.BOARD)
second  = PiZyPwm(100, 11, GPIO.BOARD)
third   = PiZyPwm(100, 12, GPIO.BOARD)
fourth  = PiZyPwm(100, 13, GPIO.BOARD)
fifth   = PiZyPwm(100, 15, GPIO.BOARD)
sixth   = PiZyPwm(100, 16, GPIO.BOARD)
seventh = PiZyPwm(100, 18, GPIO.BOARD)
eighth  = PiZyPwm(100, 22, GPIO.BOARD)

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

