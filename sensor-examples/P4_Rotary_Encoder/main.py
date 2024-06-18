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

def callback():
    global r
    
    print(f"encoder value = {r.value()}")
    sleep_ms(10)

"""
The way that the rotary encoder class works is that callbacks are triggered every time the encoder is rotated.
The callbacks are registered via the .add_listener() method, added to a list, and take no arguments.
"""

