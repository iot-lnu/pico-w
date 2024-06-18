from machine import Pin, freq
from rotary import Rotary
from config import RENDER_VALUES, CHANNEL, BRIGHTNESS, animation_amount


class RotaryIRQ(Rotary):
    __slots__ = ('_label',
                 '_pin_clk',
                 '_pin_dt',
                 'IRQ_RISING_FALLING')
    
    IRQ_RISING_FALLING = Pin.IRQ_RISING | Pin.IRQ_FALLING
    
    # GPIO pin connected to encoder CLK pin
    _pin_clk: int
    
    # GPIO pin connected to encoder DT pin
    _pin_dt: int

    # Label for this rotary encoder
    _label: str

    # Enable internal pull up resistors. -
    # Use when rotary encoder hardware lacks pull up resistors.
    pull_up: bool
    
    
    def __init__(
        self,
        pin_num_clk: int,
        pin_num_dt: int,
        label: str = None,
        min_val: int = 0,
        max_val: int = 10,
        incr: int = 1,
        reverse: bool = False,
        range_mode: int = Rotary.RANGE_UNBOUNDED,
        pull_up: bool = False,
        half_step: bool = False,
        invert=False
    ) -> None:
        super().__init__(min_val, max_val, incr, reverse, range_mode, half_step, invert)

        self._label = label

        if pull_up:
            self._pin_clk = Pin(pin_num_clk, Pin.IN, Pin.PULL_UP)
            self._pin_dt = Pin(pin_num_dt, Pin.IN, Pin.PULL_UP)
        else:
            self._pin_clk = Pin(pin_num_clk, Pin.IN)
            self._pin_dt = Pin(pin_num_dt, Pin.IN)

        self._hal_enable_irq()
    
    def label(self) -> str | None:
        return self._label

    def _enable_clk_irq(self) -> None:
        self._pin_clk.irq(self._process_rotary_pins, self.IRQ_RISING_FALLING)

    def _enable_dt_irq(self) -> None:
        self._pin_dt.irq(self._process_rotary_pins, self.IRQ_RISING_FALLING)

    def _disable_clk_irq(self) -> None:
        self._pin_clk.irq(None, 0)

    def _disable_dt_irq(self) -> None:
        self._pin_dt.irq(None, 0)

    def _hal_get_clk_value(self) -> int:
        return self._pin_clk.value()

    def _hal_get_dt_value(self) -> int:
        return self._pin_dt.value()

    def _hal_enable_irq(self) -> None:
        self._enable_clk_irq()
        self._enable_dt_irq()

    def _hal_disable_irq(self) -> None:
        self._disable_clk_irq()
        self._disable_dt_irq()

    def _hal_close(self) -> None:
        self._hal_disable_irq()


"""
Two examples of instantiating rotary encoders to control values 

ROTARYIRQ_CHANNEL = RotaryIRQ(  pin_num_clk = 18,
                                pin_num_dt = 19,
                                label = "Channel",
                                min_val = 0,
                                max_val = animation_amount - 1,
                                reverse = False,
                                range_mode = Rotary.RANGE_WRAP
                            )

ROTARYIRQ_BRIGHTNESS = RotaryIRQ(   pin_num_clk = 27,
                                    pin_num_dt = 26,
                                    label = "Brightness",
                                    min_val = 0,
                                    max_val = 20,
                                    reverse = False,
                                    range_mode = Rotary.RANGE_WRAP
                                )
"""