Raspberry Pi outlet remote
===

About
###

Control remote power sockets with a Raspberry Pi. This projects adds a web interface using the bottle.py framework.

Credits
###

+ sui li for creating [RCSwitch](https://code.google.com/p/rc-switch/) for the arduino
+ r10r for [RCSwitch Raspberry Pi port](https://github.com/r10r/rcswitch-pi)

Required Hardware
###

+ Raspberry Pi
+ 434 MHz transmitter
+ some radio controlled power sockets

Setup
###

+ install [wiringPi](https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/)
+ clone this repo `git clone https://github.com/manuelbonk/rpi-remote`
+ compile it `cd rpi-remote && make`
+ connect the transmitter's data pin to GPIO 17.
