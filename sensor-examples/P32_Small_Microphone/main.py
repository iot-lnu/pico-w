import time
from machine import ADC
from machine import Pin

# Pin setup
analogPin = ADC(27)
digitalPin = Pin(26, Pin.IN)

while True:
    analogValue = analogPin.read_u16()
    digitalValue = digitalPin.value()
    print(analogValue)
    if digitalValue == True:
        print("Digital pin activated...")
    else:
        print("Digital pin inactive...")
    time.sleep_ms(200)