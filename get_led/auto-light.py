import RPi.GPIO as GEGE

GEGE.setmode(GEGE.BCM)

led = 26

GEGE.setup(led, GEGE.OUT)

divider = 13
transistor = 6

GEGE.setup(transistor, GEGE.IN)

while True:
    led_state = not GEGE.input(transistor)
    GEGE.output(led, led_state)
