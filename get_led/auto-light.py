import RPi.GPIO as GEGE
import time

GEGE.setmode(GEGE.BCM)

led = 26

GEGE.setup(led, GEGE.OUT)

divider = 13
transistor = 6

GEGE.setup(transistor, GEGE.IN)

pause_time = 0.2

while True:
    led_state = not GEGE.input(transistor)
    GEGE.output(led, led_state)
