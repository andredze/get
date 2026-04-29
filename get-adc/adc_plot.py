import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure (figsize=(10,6))
    plt.plot   (time, voltage)
    plt.xlabel ("Time")
    plt.ylabel ("Voltage")
    plt.title  ("GRAPHIC KRUTA")
    plt.grid   (True)
    plt.savefig("plot.png")
    plt.show   ()


def plot_sampling_period_hist(time_values):
    sampling_periods = []

    for i in range(len(time_values) - 1):
        sampling_periods.append(time_values[i + 1] - time_values[i])

    plt.figure (figsize=(10, 6))
    plt.hist   (sampling_periods)
    plt.xlim   (0, 0.06)
    plt.xlabel ("Periods")
    plt.ylabel ("Count")
    plt.title  ("HISTO KRUTA")
    plt.grid   (True)
    plt.savefig("hist.png")
    plt.show   ()
    