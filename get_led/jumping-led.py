import RPi.GPIO as GEGE
import time

GEGE.setmode(GEGE.BCM)

bit_leds = [24, 22, 23, 27, 17, 25, 12, 16]

GEGE.setup(bit_leds, GEGE.OUT)

GEGE.output(bit_leds, 0)

light_time = 0.2

while True:
    for led in bit_leds:
        GEGE.output(led, 1)
        time.sleep(light_time)
        GEGE.output(led, 0)
    for led in reversed(bit_leds):
        GEGE.output(led, 1)
        time.sleep(light_time)
        GEGE.output(led, 0)