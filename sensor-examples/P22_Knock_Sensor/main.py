from machine import Pin
import time

#flags
knockState = 0
knock = Pin(27, Pin.IN)

#config
hold_time_sec = 2

#flags
last_trigger = 0

# main loop
print("Starting Detection....")
while True:
    # equivalent to if knock.value() == 1
    if knock():
        # it waits for at least 2 seconds before print
        if (knockState == 0) and (time.time() - last_trigger > hold_time_sec):
            last_trigger = time.time()
            print("Knock detected!")
            knockState = 1
    else:
        if knockState == 1:
            knockState = 0

print("Exited main loop")
