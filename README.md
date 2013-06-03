PiZyPwm
=======

PiZyPwm, for Raspberry (Pi) Ea(zy) PWM, is an easy way to implement PWM (Pulse Width Modulation) output on a Raspberry Pi using Python language.

* [Project's website](http://goddess-gate.com/projects/en/raspi/pizypwm)
* [PiZyPwm in action](http://www.youtube.com/watch?v=1X_FYJ5x6Wo)
* [PiZyPwm with a digital oscilloscope](http://www.youtube.com/watch?v=aP1F67PtaVc)


Subprojects
-----------

There are three available sub-project:
- “rpi.gpio” : if you plan to use PiZyPwm with onboard GPIO pins. It uses RPi.GPIO library, but is now obsolete as RPi.GPIO library now includes software PWM.
- “quick2wire” : if you plan to use PiZyPwm with [Quick2Wire expansion board](http://quick2wire.com/). Thanks to [SirHegel77](https://github.com/SirHegel77/) for the code.
- “mcp230xx” : if you plan to use PiZyPwm with an MCP23008 or MCP23017 GPIO expander.


Warning
-------

Due to the non real-time capacities of Python language, do not expect PWM to be very accurate. Pulses will never exactly last the theorical duration. But PiZyPwm will be enough if you don't need a great accuracy.


Example
-------

See README.md into each sub-project folder.
