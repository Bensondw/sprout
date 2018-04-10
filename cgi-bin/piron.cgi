#!/usr/bin/python

import wiringpi as wp
import time

wp.wiringPiSetupGpio()

sensor = 20
LED = 19

wp.pinMode(sensor, 0)
wp.pinMode(LED, 1)

blue = True

while blue:
	hey = wp.digitalRead(sensor)
	if hey == 1:
		print "BEN KNOBI"
		wp.digitalWrite(LED, 1)
		time.sleep(1)
	else:
		print "NO BEN"
		wp.digitalWrite(LED, 0)
		time.sleep(1)
