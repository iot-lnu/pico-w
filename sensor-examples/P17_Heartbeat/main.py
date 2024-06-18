from time import sleep_ms
from machine import ADC, Pin

analogPin = ADC(27)

while True:
    analogValue = analogPin.read_u16()
    print(f"The voltage strength of the sensor is {analogValue}")
    sleep_ms(150)