#!/usr/bin/python

import wiringpi as wp
import time

wp.wiringPiSetupGpio()

sensor = 20
LED = 19

wp.pinMode(sensor, 0)
wp.pinMode(LED, 1)

wp.digitalWrite(LED, 0)
print "NO BEN"
