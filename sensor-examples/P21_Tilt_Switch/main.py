from machine import Pin
from time import sleep_ms

tiltPin = Pin(27, Pin.IN)

while True:
    if tiltPin.value() == 1:
        print("Switch ON...")
    else:
        print("Switch OFF...")
    sleep_ms(500) 