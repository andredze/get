import mcp3021_driver as mcp_driver
import adc_plot
import time

if __name__ == "__main__":
    try:
        max_voltage = 3.296
        wait_time   = 0.001

        mcp = mcp_driver.MCP3021(max_voltage)

        voltage_values = []
        time_values    = []
        duration       = 3.0

        time_start   = time.monotonic()
        time_current = 0.0 

        while time_current < duration:
            time_current = time.monotonic() - time_start
            voltage      = mcp.get_voltage()

            voltage_values.append(voltage)
            time_values.append(time_current)
            
            time.sleep(wait_time)

        adc_plot.plot_voltage_vs_time(time_values, \
            voltage_values, max_voltage)
        
        print(voltage_values)
        print(time_values)

        adc_plot.plot_sampling_period_hist(time_values)
    
    except KeyboardInterrupt:
        print("\nEnddnNDndnaajn")

    finally:
        mcp.__dtor__()