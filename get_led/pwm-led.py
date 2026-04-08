import RPi.GPIO as GEGE
import time

GEGE.setmode(GEGE.BCM)

led = 26

GEGE.setup(led, GEGE.OUT)

pwm = GEGE.PWM(led, 200)

duty = 0.0

pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0