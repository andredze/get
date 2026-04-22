import numpy
import time as timelib

def get_sin_wave_amplitude(freq, time):
    value = numpy.sin(2 * freq * time * numpy.pi)
    value = (value + 1) * 0.5
    return value


def wait_for_sampling_period(sampling_frequency):
    time = 1 / sampling_frequency
    timelib.sleep(time)


def get_triangle_amplitude(freq, time):
    period = 1 / freq
    
    norm = time % period

    if (norm <= period / 2):
        value = 1 - norm * (2 / period)
    else:
        value = -1 + norm * (2 / period)
    
    return value
