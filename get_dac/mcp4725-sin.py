import mcp4725_driver as mcp
import signal_generator as sg
import time as timelib


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(4.2, 0x61, True)

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