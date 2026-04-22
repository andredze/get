import RPi.GPIO as GEGE

def safe_num(num):
    if num < 0:
        return 0
    
    elif num > 255:
        return 255

    return num


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


class R2R_DAC:
    def __init__(self, gege_bits, dynamic_range, verbose = False):
        self.gege_bits     = gege_bits
        self.dynamic_range = dynamic_range
        self.verbose       = verbose

        GEGE.setmode(GEGE.BCM)
        GEGE.setup(self.gege_bits, GEGE.OUT, initial = 0)
    
    def dtor(self):
        GEGE.output(self.gege_bits, 0)
        GEGE.cleanup()
    
    def set_number(self, number):
        bin_values_list = dec2bin(safe_num(number))
        GEGE.output(self.gege_bits, bin_values_list)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапозон ЦАП \
                  (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            return
        else:
            number = int(voltage / self.dynamic_range * 255)
        
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
            
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Try again")
    
    except KeyboardInterrupt:
        print()
        print("Конец программы")

    finally:
        dac.dtor()
