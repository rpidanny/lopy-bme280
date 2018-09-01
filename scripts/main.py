# main.py -- put your code here!
import time
from machine import I2C
from network import WLAN

from mqtt import MQTTClient
from bme280 import BME280, BME280_OSAMPLE_16

from config import adafruit, known_nets
from util.wifi import connect_wifi


i2c = I2C(0, I2C.MASTER, baudrate=400000)
bme = BME280(i2c=i2c, mode=BME280_OSAMPLE_16)

wl = WLAN()

client = MQTTClient(
    "lopy-nl",
    "io.adafruit.com",
    user=adafruit['user'],
    password=adafruit['apikey'],
    port=1883)

client.connect()

while True:
    print("Temp: " + bme.temperature + ", Pressure: " + bme.pressure +
          ", Humidity: " + bme.humidity)
    if not wl.isconnected():
        connect_wifi(known_nets)
        client.connect()
    client.publish(topic=adafruit['user'] + "/feeds/bme280_temp", msg=bme.temperature)
    client.publish(topic=adafruit['user'] + "/feeds/bme280_pressure", msg=bme.pressure)
    client.publish(topic=adafruit['user'] + "/feeds/bme280_humidity", msg=bme.humidity)
    time.sleep(10)
