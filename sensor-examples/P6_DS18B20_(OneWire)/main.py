import machine
import onewire
import ds18x20
from time import sleep, sleep_ms
 
oneWire_pin = machine.Pin(27)   # DS18x20 connected to pin 27
# Initailize pin with Dallas Semiconductor temperature sensor DS18X20 
oneWire_sensor = ds18x20.DS18X20(onewire.OneWire(oneWire_pin))

# Scan and print the address of all sensors connected to pin 27 
sensors = oneWire_sensor.scan()
print('Found devices: ', sensors)
 
while True:
    oneWire_sensor.convert_temp()
    sleep_ms(750)

    for sensor in sensors:
        print(f"Sensor address is: {sensor}")
        print(f"Temperature is {oneWire_sensor.read_temp(sensor)} deg Celsius")
    sleep(2)