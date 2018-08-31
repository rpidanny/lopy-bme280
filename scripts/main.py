# main.py -- put your code here!
import time
from machine import I2C
from mqtt import MQTTClient
from bme280 import BME280, BME280_OSAMPLE_16
from config import adafruit


def sub_cb(topic, msg):
    print(msg)


i2c = I2C()
bme = BME280(i2c=i2c, mode=BME280_OSAMPLE_16)

client = MQTTClient(
    "lopy-nl",
    "io.adafruit.com",
    user=adafruit['user'],
    password=adafruit['apikey'],
    port=1883)

client.set_callback(sub_cb)
client.connect()
# client.subscribe(topic="rpidanny/feeds/lopy-nl")

while True:
    print("Temp: " + bme.temperature + ", Pressure: " + bme.pressure +
          ", Humidity: " + bme.humidity)
    client.publish(topic=adafruit['user'] + "/feeds/bme280_temp", msg=bme.temperature)
    client.publish(topic=adafruit['user'] + "/feeds/bme280_pressure", msg=bme.pressure)
    client.publish(topic=adafruit['user'] +  "/feeds/bme280_humidity", msg=bme.humidity)
    time.sleep(10)
