import time
from machine import ADC
from machine import Pin

analogPin = ADC(27)

while True:
    analogValue = analogPin.read_u16()
    print("The voltage strength of the sensor is {}".format(analogValue))
    time.sleep(1)