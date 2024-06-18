# Link: https://github.com/kfricke/micropython-sht31

from machine import I2C, SoftI2C
import time
from typing import *

R_HIGH   = const(1)
R_MEDIUM = const(2)
R_LOW    = const(3)

class SHT31(object):
    """
    This class implements an interface to the SHT31 temprature and humidity
    sensor from Sensirion.
    """
    
    __slots__:Tuple[str] = (
                '_i2c',
                '_addr',
                '_map_cs_r'
                )

    # This static map helps keeping the heap and program logic cleaner
    _map_cs_r: Dict[bool, Dict[int, bytes]] = {
        True: {
            R_HIGH : b'\x2c\x06',
            R_MEDIUM : b'\x2c\x0d',
            R_LOW: b'\x2c\x10'
            },
        False: {
            R_HIGH : b'\x24\x00',
            R_MEDIUM : b'\x24\x0b',
            R_LOW: b'\x24\x16'
            }
        }

    def __init__(self, i2c: I2C | SoftI2C, addr: bytes = 0x44) -> None:
        """
        Initialize a sensor object on the given I2C bus and accessed by the
        given address.
        """
        if i2c == None: raise ValueError('I2C object needed as argument!')
        self._i2c = i2c
        self._addr = addr

    def _send(self, buf: bytes) -> None:
        """
        Sends the given buffer object over I2C to the sensor.
        """
        self._i2c.writeto(self._addr, buf)

    def _recv(self, count: int) -> bytes:
        """
        Read bytes from the sensor using I2C. The byte count can be specified
        as an argument.
        Returns a bytes object for the result.
        """
        return self._i2c.readfrom(self._addr, count)

    def _raw_temp_humi(self, r: int = R_HIGH, cs: bool = True) -> Tuple[float, float]:
        """
        Read the raw temperature and humidity from the sensor and skips CRC
        checking.
        Returns a tuple for both values in that order.
        """
        if r not in (R_HIGH, R_MEDIUM, R_LOW):
            raise ValueError('Wrong repeatabillity value given!')
        self._send(self._map_cs_r[cs][r])
        time.sleep_ms(50)
        raw = self._recv(6)
        return (raw[0] << 8) + raw[1], (raw[3] << 8) + raw[4]

    def get_temp_humi(self, resolution: int = R_HIGH, clock_stretch: bool = True, celsius: bool = True) -> Tuple[float]:
        """
        Read the temperature in degree celsius or fahrenheit and relative
        humidity. Resolution and clock stretching can be specified.
        Returns a tuple for both values in that order.
        """
        t, h = self._raw_temp_humi(resolution, clock_stretch)
        if celsius:
            temp = -45 + (175 * (t / 65535))
        else:
            temp = -49 + (315 * (t / 65535))
        return temp, 100 * (h / 65535)