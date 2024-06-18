from machine import Pin
from time import sleep_ms

# Set the led and sensor pin 
led = Pin("LED", Pin.OUT)
sensor = Pin(27, Pin.IN)

state = True

while True:
    state = sensor.value()
    if state == False:
        led.on()
        print("Detected...")
    else:
        led.off()
        print("Safe to go...")
    sleep_ms(20)