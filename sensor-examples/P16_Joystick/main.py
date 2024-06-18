
from machine import Pin, ADC
from time import sleep_ms

# Pin setup
xAxisPin = ADC(Pin(28))
yAxisPin = ADC(Pin(27))
buttonPin = Pin(26,Pin.IN, Pin.PULL_UP)

# Initializing the input button
buttonPin.value(1)

while True:
    xAxisValue = xAxisPin.read_u16()
    yAxisValue = yAxisPin.read_u16()
    buttonValue = buttonPin.value()

    xAxisStatus = "center"
    yAxisStatus = "center"
    buttonStatus = "not pressed"

    if xAxisValue <= 600:
        xAxisStatus = "south"
    elif xAxisValue >= 60000:
        xAxisStatus = "north"
    if yAxisValue <= 600:
        yAxisStatus = "east"
    elif yAxisValue >= 60000:
        yAxisStatus = "west"
    if buttonValue == 0:
        buttonStatus = "pressed"
    
    print(f"xAxis value is {xAxisValue} toward {xAxisStatus}\nyAxis value is {yAxisValue} toward {yAxisStatus}\nButten is {buttonStatus}\n")
    
    sleep_ms(500)