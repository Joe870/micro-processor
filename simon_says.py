from machine import Pin
import utime
import random

yellow = Pin(0, Pin.OUT)
green = Pin(1, Pin.OUT)
blue = Pin(2, Pin.OUT)

yellow_button = Pin(3, Pin.IN)
green_button = Pin(4, Pin.IN)
blue_button = Pin(5, Pin.IN)

leds = [yellow, green, blue]
amountShow = 2

while True:
    amountShow += 1
    order = []
    playerInput = []
    for x in range(amountShow):
        randomValue = random.randint(0, 2)
        ledColor = leds[randomValue]
        order.append(ledColor)
    for color in order:
        color.toggle()
        utime.sleep(1)
        color.toggle()
        utime.sleep(0.5)
    while len(playerInput) < amountShow:
        utime.sleep(0.01)
        if yellow_button.value() == 1:
            playerInput.append(yellow)
            utime.sleep(0.3)
        if green_button.value() == 1:
            playerInput.append(green)
            utime.sleep(0.3)
        if blue_button.value() == 1:
            playerInput.append(blue)
            utime.sleep(0.3)
    if order == playerInput:
        print("correct")
    else:
        print("incorrect")