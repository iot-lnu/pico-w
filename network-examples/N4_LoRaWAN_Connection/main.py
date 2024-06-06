import struct
import time
from LoRaWAN import lora

lora = lora()

APP_EUI = "0000000000001234"                   # Substitute Your APP_EUI here
DEV_EUI = "70B3D57ED005E758"                   # Substitute Your DEV_EUI here
APP_KEY = "31CC62B0256EA3311EEFDCB9ED2CEC3B"   # Substitute Your APP_KEY here

lora.configure(DEV_EUI, APP_EUI, APP_KEY)

lora.startJoin()
print("Start Join.....")
while not lora.checkJoinStatus():
  print("Joining....")
  time.sleep(1)
print("Join success!")

# Reading from sensor should be done here

# Example temperature (in Celsius) and humidity (%) values with a negative temperature
temperature, humidity = -14.2, 42.5

# Convert the float values to integers by multiplying them by a factor (example: 10)
temp_int = int(temperature * 10)
humidity_int = int(humidity * 10)

# https://docs.micropython.org/en/latest/library/struct.html
# >: Indicates big-endian byte order. Big-endian means the most significant byte is stored first.
# h: Represents a short integer (2 bytes).
# H: Represents an unsigned short integer (2 bytes).
payload = struct.pack(">hH", temp_int, humidity_int)
payload = payload.hex()


while True:
  lora.sendMsg(payload)
  print("Sent message:", payload)

  response = lora.receiveMsg()

  if (response != ""):
    print("Received: ", end=": ")
    print(response) 

  
  time.sleep(30)