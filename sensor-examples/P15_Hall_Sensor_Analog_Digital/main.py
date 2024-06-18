from time  import sleep_ms
from machine import ADC, Pin

# Pin setup
#analogPin = ADC(27)
digitalPin = Pin(27, Pin.IN)

while True:
    #analogValue = analogPin.read_u16()
    digitalValue = digitalPin.value()
    #print(f"The magnetic strength is {analogValue}")  # The stronger magnet the lower value it produce
    if digitalValue == False:     # if your sensor prints reverse when there is no magnetic field change this False to True 
        print("Digital pin activated...")
    else:
        print("Digital pin inactive...")
    
    sleep_ms(50)