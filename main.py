import INA226
from time import sleep
from machine import Pin, I2C
import display
# i2c
i2c = I2C(0)
# ina226
ina = INA226.INA226(i2c, 0x40)
# default configuration and calibration value
ina.set_calibration()
print(ina.bus_voltage)
print(ina.shunt_voltage)
print(ina.current)
print(ina.power)

