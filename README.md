PiZyPwm
=======

PiZyPwm, for Raspberry (Pi) Ea(zy) PWM, is an easy way to implement PWM (Pulse Width Modulation) output on a Raspberry Pi using Python language.

* [PiZyPwm in action](http://www.youtube.com/watch?v=1X_FYJ5x6Wo)
* [PiZyPwm with a digital oscilloscope](http://www.youtube.com/watch?v=aP1F67PtaVc)


Subprojects
-----------

There are two available subproject:
- “rpi.gpio” : if you plan to use PiZyPwm with onboard GPIO pins. It uses RPi.GPIO library, but is now obsolete as RPi.GPIO library now includes software PWM.
- “quick2wire” : if you plan to use PiZyPwn with [Quick2Wire expansion board](http://quick2wire.com/). Thanks to [SirHegel77](https://github.com/SirHegel77/) for the code.


Warning
-------

Due to the non real-time capacities of Python language, do not expect PWM to be very accurate. Pulses will never exactly last the theorical duration. But PiZyPwn will be enough if you don't need a great accuracy.


Example
-------

See README.md into each subproject folder.
