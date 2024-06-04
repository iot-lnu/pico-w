import time
from machine import ADC
from machine import Pin


# Pin setup
soil = ADC(27)
min_moisture=0
max_moisture=65535

while True:
    try:
        moisture = round((max_moisture-soil.read_u16())*130/(max_moisture-min_moisture))
        if(moisture >= 0 and moisture <= 100):
            print("Moisture is {}%".format(moisture))
    except Exception as error:
        print("Exception occurred", error)
    
    time.sleep(1)

