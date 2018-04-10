#!/usr/bin/python

import threading #don't forget sudo chmod 777 /dev/ttyS0
import time
import serial
import bluetooth

ser = serial.Serial('/dev/ttyS0', 9600, timeout=None)
#ser.open()

def serialWrite():
  result = bluetooth.lookup_name('A0:99:9B:36:36:A5', timeout=5)
  if (result != None):
     print("here")
     ser.write("prep\n")
  else:
     print "nada"


try:
  serialWrite()
  print "Exiting main thread"
  ser.close()

except KeyboardInterrupt:
    ser.close()
