from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT22(Pin(15))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature:' %temp)
    print('Humidity:' %hum)
  except OSError as e:
    print('Failed to read sensor.')