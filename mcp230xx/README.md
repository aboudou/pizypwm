PiZyPwm (MCP230XX flavor)
=========================

PiZyPwm, for Raspberry (Pi) Ea(zy) PWM, is an easy way to implement PWM (Pulse Width Modulation) output on a Raspberry Pi using Python language.

* [PiZyPwm in action](http://www.youtube.com/watch?v=1X_FYJ5x6Wo)
* [PiZyPwm with a digital oscilloscope](http://www.youtube.com/watch?v=aP1F67PtaVc)


Warning
-------

Due to the non real-time capacities of Python language, do not expect PWM to be very accurate. Pulses will never exactly last the theorical duration. But PiZyPwm will be enough if you don't need a great accuracy.


Running example.py
------------------

To run this example code, you'll need the assembly you'll find [here](https://github.com/aboudou/movingraspi/blob/master/Documentation/MovingRaspi%20concept.fzz?raw=true) (You'll have to open it with [Fritzing](http://fritzing.org/))

Requirements
------------

* First of all : a Raspberry Pi
* Python (with Debian / Raspbian : packages “python” and “python-dev”)
* SMBus library . On Raspbian, install package “python-smbus”.
* Adafruit MCP230xx library (See below).
* Adafruit I2C library (See below).


Installing Adafruit libraries
-----------------------------

Go into “Server” folder, then execute the following commands (you may need to install “curl” before) :
`curl -O https://raw.github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/master/Adafruit_I2C/Adafruit_I2C.py`
`curl -O https://raw.github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/master/Adafruit_MCP230xx/Adafruit_MCP230xx.py`

Depending on the date you got Adafruit\_MCP230xx.py, you may have a version which works with MCP23017 chip, but not with MCP23008 chip.

* If you have downloaded the file starting December 28, 2012, it will be OK.
* If you have downloaded the file before December 27, 2012, you'll have to download it again.
* If you have downloaded the file on December 27, 2012, check at the beginning of the file for the following lines of code :

```
MCP23008_GPIOA  = 0x09
MCP23008_GPPUA  = 0x06
MCP23008_OLATA  = 0x0A
```

If they are present, you have the correct version of the file. If not, you have to download it again.


Example usage
-------------

    import RPi.GPIO as GPIO
    
    from pizypwm import *
  
    # Set GPIO pin #0 as PWM output with a frequency of 100 Hz, on a MCP23008 chip (8 GPIO) at address 0x20 on I2C bus
    pwm = PiZyPwm(100, 0, 0x20, 8)
    
    # Start PWM output with a duty cycle of 20%. The pulse (HIGH state) will have a duration of
    # (1 / 100) * (20 / 100) = 0.002 seconds, followed by a low state with a duration of
    # (1 / 100) * ((100 - 20) / 100) = 0.008 seconds.
    # If a LED is plugged to with GPIO pin, it will shine at 20% of its capacity.
    pwm.start(20)
    
    # Change duty cycle to 6%. The pulse (HIGH state) will now have a duration of
    # (1 / 100) * (6 / 100) = 0.0006 seconds, followed by a low state with a duration of
    # (1 / 100) * ((100 - 6) / 100) = 0.0094 seconds.
    # If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity.
    pwm.changeDutyCycle(6)
    
    # Change the frequency of the PWM pattern. The pulse (HIGH state) will now have a duration of
    # (1 / 10) * (6 / 100) = 0.006 seconds, followed by a low state with a duration of
    # (1 / 10) * ((100 - 6) / 100) = 0.094 seconds.
    # If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity, but you may
    # notice flickering.
    pwm.changeFrequency(10)
    
    # Stop PWM output
    pwm.stop()

