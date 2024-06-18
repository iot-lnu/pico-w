# MIT License (MIT)
# Copyright (c) 2021 Mike Teachman
# https://opensource.org/licenses/MIT

# example for MicroPython rotary encoder

from rotary_irq_rp2 import RotaryIRQ
from time import sleep_ms


r = RotaryIRQ(pin_num_clk=26,
              pin_num_dt=27,
              min_val=0,
              max_val=20,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_WRAP)

"""
You can set an initial value to the rotary encoder using .set().
We use 0 here but it can be anything.
"""
r.set(value = 0)


"""
The way that the rotary encoder class works is that callbacks are triggered every time the encoder is rotated.
The callbacks are registered via the .add_listener() method, added to a list, and take no arguments.
The callbacks are registered as hardware interrupts, and therefore will interrupt already running code.
It's best to keep these short and only do a few things in them.
"""


def callback() -> None:
    """
    This function is a callback function for the rotary encoder.
    It is triggered every time the encoder is rotated.
    """
    global r
    
    print(f"encoder value = {r.value()}")
    sleep_ms(10)
    

r.add_listener(callback)

  
"""
So now we could some sorta code running. Here we just do an infinte loop.
"""
while True: 
    r.value()