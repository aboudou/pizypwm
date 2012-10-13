PiZyPwm
=======

PiZyPwm, for Raspberry (Pi) Ea(zy) PWM, is an easy way to implement PWM (Pulse Width Modulation) output on a Raspberry Pi using Python language.

* [Youtube video](http://www.youtube.com/watch?v=1X_FYJ5x6Wo)


Warning
-------

Due to the non real-time capacities of Python language, do not expect PWM to be very accurate. Pulses will never exactly last the theorical duration. But PiZyPwn will be enough if you don't need a great accuracy.



Requirements
------------

* First of all : a Raspberry Pi
* Python (with Debian / Raspbian : packages “python” and “python-dev”)
* RPi.GPIO library (0.4.0a or newer). On Raspbian, install package “python-rpi.gpio”.


Example usage
-------------

    import RPi.GPIO as GPIO
    
    from pizypwm import *
  
    # Set GPIO pin #7 as PWM output with
    # - A base time of 0.01 second
    # - 100 slices of base time (a pulse - HIGH state will have a minimal duration 
    #   of 0.01 / 100 = 0.0001 seconds)
    pwm = PiZyPwm(0.01, 100, 7, GPIO.BOARD)
    
    # Start PWM output. The pulse (HIGH state) will have a duration of
    # (0.01 / 100) * 20 = 0.002 seconds, followed by a low state with a duration of
    # (0.01 / 100) * (100 - 20) = 0.008 seconds.
    # If a LED is plugged to with GPIO pin, it will shine at 20% of its capacity
    pwm.start(20)
    
    # Change number of slice of HIGH state. The pulse (HIGH state) will now have a duration of
    # (0.01 / 100) * 6 = 0.0006 seconds, followed by a low state with a duration of
    # (0.01 / 100) * (100 - 6) = 0.0094 seconds
    # If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity
    pwm.changeNbSlicesOn(6)
    
    # Change the base time of the PWM pattern. The pulse (HIGH state) will now have a duration of
    # (0.1 / 100) * 6 = 0.006 seconds, followed by a low state with a duration of
    # (0.1 / 100) * (100 - 6) = 0.094 seconds
    # If a LED is plugged to with GPIO pin, it will shine at 60% of its capacity, but you may
    # notice flickering
    pwm.changeBaseTime(0.1)
    
    # Change the number of slices PWM pattern. The pulse (HIGH state) will now have a duration of
    # (0.1 / 10) * 6 = 0.06 seconds, followed by a low state with a duration of
    # (0.1 / 10) * (10 - 6) = 0.94 seconds
    # If a LED is plugged to with GPIO pin, it will shine at 60% of its capacity, but you will
    # probably notice flickering
    pwm.changeNbSlices(10)
    
    # Stop PWM output
    pwm.stop()

