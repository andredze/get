import RPi.GPIO as GEGE

class PWM_DAC:
    def __init__(self, gege_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gege_pin      = gege_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        
        GEGE.setmode(GEGE.BCM)
        GEGE.setup(self.gege_pin, GEGE.OUT, initial = 0)
        
        self.pwm = GEGE.PWM(self.gege_pin, self.pwm_frequency)
        self.pwm.start(0)

    def dtor(self):
        try:
            self.pwm.ChangeDutyCycle(0)
            self.pwm.stop()

        finally:
            GEGE.output(self.gege_pin, 0)
            GEGE.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапозон ЦАП \
                  (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            duty = 0
            
        else:
            duty = int(voltage / self.dynamic_range * 100)
        
        self.pwm.ChangeDutyCycle(duty)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

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