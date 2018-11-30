# Load default libs
from machine import Pin

# Settings the vars
relay = Pin(5, Pin.OUT)
sensor = Pin(4, Pin.IN, Pin.PULL_UP)

# The actual program
while True:
  if sensor.value():
    relay.off()
  else:
    relay.on()
