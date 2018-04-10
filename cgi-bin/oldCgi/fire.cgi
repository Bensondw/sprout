#!/usr/bin/python

import threading, time, serial, bluetooth

ser = serial.Serial('/dev/ttyS0', 9600, timeout=None)
#ser.open()

def serialWrite():
  result = bluetooth.lookup_name('A0:99:9B:36:36:A5', timeout=5)
  if (result != None):
     ser.write("fire\n")


try:
  serialWrite()
  print "Exiting main thread"
  ser.close()

except KeyboardInterrupt:
    ser.close()
