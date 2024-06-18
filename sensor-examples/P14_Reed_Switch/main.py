from machine import Pin
from time import sleep_ms

# Set the pin for reed switch
reed_switch = Pin(27, Pin.IN)

while True:
    value = reed_switch.value()
    
    if value == 1:
        print("Magnet Detected...")
    else:
        print("No Magnetic Field...")
    
    sleep_ms(50)