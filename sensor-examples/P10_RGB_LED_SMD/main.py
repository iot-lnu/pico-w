from machine import Pin
from time import sleep

LED_Pin_Red = Pin(26, Pin.OUT)
LED_Pin_Green = Pin(27, Pin.OUT)
LED_Pin_Blue = Pin(28, Pin.OUT)

while True:
    LED_Pin_Red.value(0)
    LED_Pin_Green.value(0)
    LED_Pin_Blue.value(0)
    sleep(1)
    
    LED_Pin_Red.value(0)
    LED_Pin_Green.value(0)
    LED_Pin_Blue.value(1)
    sleep(1)

    LED_Pin_Red.value(0)
    LED_Pin_Green.value(1)
    LED_Pin_Blue.value(0)
    sleep(1)

    LED_Pin_Red.value(0)
    LED_Pin_Green.value(1)
    LED_Pin_Blue.value(1)
    sleep(1)

    LED_Pin_Red.value(1)
    LED_Pin_Green.value(0)
    LED_Pin_Blue.value(0)
    sleep(1)

    LED_Pin_Red.value(1)
    LED_Pin_Green.value(0)
    LED_Pin_Blue.value(1)
    sleep(1)

    LED_Pin_Red.value(1)
    LED_Pin_Green.value(1)
    LED_Pin_Blue.value(0)
    sleep(1)

    LED_Pin_Red.value(1)
    LED_Pin_Green.value(1)
    LED_Pin_Blue.value(1)
    sleep(1)
