#!/usr/bin/python

import os

os.system("gpio pwm 1 350")
os.system("gpio -g write 19 0")
os.system("gpio -g write 20 1")
os.system("gpio -g write 21 1")


