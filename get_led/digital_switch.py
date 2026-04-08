import RPi.GPIO as GEGE
import time

GEGE.setmode(GEGE.BCM)

led = 26

GEGE.setup(led, GEGE.OUT)

button = 13

GEGE.setup(button, GEGE.IN)

pause_time = 0.2

state = 0

while True:
    if GEGE.input(button) == 1:
        state = not state
        GEGE.output(led, state)
        time.sleep(pause_time)

