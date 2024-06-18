from machine import Pin
from time import sleep_ms

vibratePin = Pin(27, Pin.IN)

while True:
    if vibratePin.value() == 1:
        print("No vibration...")
    else:
        print("Vibration detected...")
    sleep_ms(500) 