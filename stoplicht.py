from machine import Pin
from hcsr04 import HCSR04
import utime
import random
import time
from time import sleep

sensor = HCSR04(trigger_pin=8, echo_pin=7, echo_timeout_us=10000)
red_led = Pin(0, Pin.OUT)
yellow_led = Pin(2, Pin.OUT)
green_led = Pin(3, Pin.OUT)
last_time = time.ticks_ms()

while True:
    afstand = sensor.distance_cm()
    print("Afstand: {:.2f} cm".format(afstand))
    if afstand <= 10:
        red_led.toggle()
        yellow_led.toggle()
        green_led.toggle()
        sleep(0.5)
    else:
        print("ik ben in de else")
        red_led.off()
        yellow_led.off()
        green_led.off()
        current_time = time.ticks_ms()
        delta_time = time.ticks_diff(current_time, last_time)
        print('dit is de deltatime' + str(delta_time))
        print('dit is de last time' + str(last_time))
        print('dit is de current time' + str(current_time))
        if delta_time < 5000:
            red_led.on()
        if delta_time >= 5000 and delta_time < 10000:
            red_led.off()
            green_led.on()
            current_time = time.ticks_ms()
            print(current_time)
            print('ik ben in de eerste if')
            print(delta_time)
        elif delta_time >= 10000 and delta_time < 13000:
            green_led.off()
            yellow_led.on()
            print('ik ben in de tweede if')
            print(delta_time)
        elif delta_time >= 13000 and delta_time < 16000:
            yellow_led.off()
            red_led.on()
            print('ik ben in de derde if')
            print(delta_time)
        elif delta_time >= 18000:
            red_led.off()
            yellow_led.off()
            green_led.off()
            print('ik ben in de laatste if')
            print(delta_time)
