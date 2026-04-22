import RPi.GPIO as GEGE

GEGE.setmode(GEGE.BCM)

leds = [16, 20, 21, 25, 26, 17, 27, 22]
GEGE.setup(leds, GEGE.OUT)

GEGE.output(leds, 0)

dynamic_range = 3.15

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапозон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def safe_num(num):
    if num < 0:
        return 255
    
    elif num > 255:
        return 0

    return num


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def number_to_dac(number):
    bin_values_list = dec2bin(safe_num(number))
    GEGE.output(leds, bin_values_list)


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Try again")

except KeyboardInterrupt:
    print()
    print("Конец программы")

finally:
    GEGE.output(leds, 0)
    GEGE.cleanup()
