from machine import Pin, time_pulse_us
import time

# Define constants
SOUND_SPEED = 340 
TRIG_PULSE_DURATION_US=10

# Pin setup
trigPin = Pin(26, Pin.OUT)
echoPin = Pin(27, Pin.IN)

# Initialize pin
trigPin.value(0)
time.sleep_us(5)

while True:
    trigPin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trigPin.value(0)

    ultrason_duration = time_pulse_us(echoPin, 1, 30000)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    print(f"Distance to object is {distance_cm} centimeter")
    time.sleep_ms(500)