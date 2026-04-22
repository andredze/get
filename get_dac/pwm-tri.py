import pwm_dac
import signal_generator as sg
import time as timelib


amplitude = 1.2
signal_frequency = 6
sampling_frequency = 3000


if __name__ == "__main__":
    try:
        dac = pwm_dac.PWM_DAC(12, 500, amplitude, True)

        while True:
            try:
                curr_ampl = sg.get_triangle_amplitude(signal_frequency, timelib.monotonic())
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