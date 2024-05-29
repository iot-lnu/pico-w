from machine import Pin
import time

# Set the pin for reed switch
reed_switch = Pin(27, Pin.IN)

while True:
    value = reed_switch.value()
    
    if value == 1:
        print("Magnet Detected...")
    else:
        print("No Magnetic Field...")
    
    time.sleep(1)