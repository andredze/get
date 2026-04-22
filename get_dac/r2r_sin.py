import r2r_dac as r2r
import signal_generator as sg
import time as timelib


amplitude = 3.2
signal_frequency = 1
sampling_frequency = 10000


if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], amplitude, True)
            
        while True:
            try:
                curr_ampl = sg.get_sin_wave_amplitude(signal_frequency, timelib.monotonic())
                # print(curr_ampl)
                # print(curr_ampl*amplitude)
                dac.set_voltage(curr_ampl * amplitude)
                sg.wait_for_sampling_period(sampling_frequency)
                
            except ValueError:
                print("Вы ввели не число. Try again")
    
    except KeyboardInterrupt:
        print()
        print("Конец программы")

    finally:
        dac.dtor()