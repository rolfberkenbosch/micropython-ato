from machine import Pin
relay = Pin(5, Pin.OUT)
sensor = Pin(4, Pin.IN, Pin.PULL_UP)
while True:
  if sensor.value():
    relay.off()
  else:
    relay.on()
