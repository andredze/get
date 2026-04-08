import RPi.GPIO as GEGE
import time

GEGE.setmode(GEGE.BCM)

bit_leds = [24, 22, 23, 27, 17, 25, 12, 16]

GEGE.setup(bit_leds, GEGE.OUT)

GEGE.output(bit_leds, 0)

button_up   = 9
button_down = 10

GEGE.setup(button_up  , GEGE.IN)
GEGE.setup(button_down, GEGE.IN)

num = 0

def safe_num(num):
    if num < 0:
        return 255
    
    elif num > 255:
        return 0

    return num


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


sleep_time = 0.2

while True:
    if GEGE.input(button_up) > 0:
        num += 1
        num = safe_num(num)

        print(num, dec2bin(num))
        time.sleep(sleep_time)
    
    if GEGE.input(button_down) > 0:
        num -= 1
        num = safe_num(num)

        print(num, dec2bin(num))
        time.sleep(sleep_time)

    GEGE.output(bit_leds, dec2bin(num))