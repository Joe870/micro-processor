from hcsr04 import HCSR04
from time import sleep

# Maak een HCSR04-object aan met de juiste GPIO-pinnen voor trigger en echo
sensor = HCSR04(trigger_pin=8, echo_pin=7, echo_timeout_us=10000)

while True:
    # Meet de afstand en druk deze af
    try:
        afstand = sensor.distance_cm()
        print("Afstand: {:.2f} cm".format(afstand))
    except OSError as e:
        print("Sensorfout:", e)

    # Wacht een seconde voordat je opnieuw meet
    sleep(1)