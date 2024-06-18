from time import sleep
from machine import ADC
from math import log

# Constants
BETA = 3950
KELVIN_CONSTANT = 273.15

# ADC conversion function to give Celsius
def adc_to_celsius(x: float) -> float:
    return(1 / (log(1 / (65535 / x - 1)) / BETA + 1 / 298.15) - KELVIN_CONSTANT)

# Pin Setup
thermistor_pin = ADC(27)

while True:
    thermistor_value = thermistor_pin.read_u16()
    print(f"Thermistor value is {thermistor_value} after conversion to Celsius we got {adc_to_celsius(thermistor_value)} degrees Celsius")
    sleep(2)