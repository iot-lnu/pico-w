import dht
import machine
from time import sleep

"""
Unlike most of the sensors used in the other script, the dht11 and dht22 are included in micropython for the pico. 
THis means we dont need some third-party library.
"""
tempSensor = dht.DHT11(machine.Pin(27))     # DHT11 Constructor 
# tempSensor = dht.DHT22(machine.Pin(27))   # DHT22 Constructor

while True:
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print(f"Temperature is {temperature} deg Celsius and Humidity is {humidity}%")
    except Exception as error:
        print("Exception occurred", error)
    sleep(2)