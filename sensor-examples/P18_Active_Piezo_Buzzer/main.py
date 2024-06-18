from machine import Pin
from time import sleep
 
buzzer = Pin(27, Pin.OUT)
 
while True:
    buzzer.value(1)
    print("Buzzer active...")
    sleep(1)
    buzzer.value(0)
    print("Buzzer inactive...")
    sleep(1)