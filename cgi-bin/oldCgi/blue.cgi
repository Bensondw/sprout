#!/usr/bin/python

import bluetooth
import time
import json

print "Content-type: application/json"
print

result = bluetooth.lookup_name('A0:99:9B:36:36:A5', timeout=5)
if (result != None):
    response = "In Range Tarkin"
else:
     response = "Out of Sight Out of Mind"

print(json.JSONEncoder().encode(response))
