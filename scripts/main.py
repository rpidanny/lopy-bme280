# main.py -- put your code here!
import time
from machine import I2C
from bme280 import BME280

i2c = I2C()
bme = BME280(i2c=i2c)

while True:
  print("Temp: "+ bme.temperature + ", Pressure: " + bme.pressure +", Humidity: " + bme.humidity)
  time.sleep(1)
