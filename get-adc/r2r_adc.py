import RPi.GPIO as GEGE
import time
from get_bin_list import get_bin

class R2R_ADC:
    def __init__(self, dynamic_range, \
                 compare_time = 0.005, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose       = verbose
        self.compare_time  = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        
        GEGE.setmode(GEGE.BCM)
        GEGE.setup  (self.bits_gpio, GEGE.OUT, initial = 0)
        GEGE.setup  (self.comp_gpio, GEGE.IN)
        return

    def __dtor__(self):
        GEGE.output(self.bits_gpio, 0)
        GEGE.cleanup()
        return

    def number_to_dac(self, number):
        value = get_bin(number)
        GEGE.output(self.bits_gpio, value)
        return

    def sequential_counting_adc(self):
        levels = 256

        for number in range(levels):
            self.number_to_dac(number)

            voltage = number / levels * self.dynamic_range

            comp = GEGE.input(self.comp_gpio)

            if comp == 1:
                print("Reached ADC voltage of {:.2f}".format(voltage))
                return number

            time.sleep(self.compare_time)

        return levels - 1 
        

    def get_sc_voltage(self):
        number  = self.sequential_counting_adc()
        voltage = number / 256 * self.dynamic_range
        return voltage


if __name__ == "__main__":
    
    adc = R2R_ADC(3.296)
    
    try:    
        while True:
            curr_voltage = adc.get_sc_voltage()
            
            print(f"Current voltage: {curr_voltage}")

    except KeyboardInterrupt:
        print("\nEnddd")

    finally:
        adc.__dtor__()


