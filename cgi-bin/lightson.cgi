#!/usr/bin/python

import wiringpi as wp

wp.wiringPiSetupGpio()

wp.pinMode(19, 1)

wp.digitalWrite(19, 1)
