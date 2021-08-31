# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin, PWM
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'vivo1808'
password = '77777777'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

Mot_R_direction = Pin(0, Pin.OUT)
Mot_L_direction = Pin(2, Pin.OUT)
Mot_R_speed = PWM(Pin(5), 5000)
Mot_L_speed = PWM(Pin(4), 5000)
