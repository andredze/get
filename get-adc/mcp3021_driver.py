import RPi.GPIO as GEGE
import smbus


class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus           = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address       = 0x4D
        self.verbose       = verbose
        return

    def __dtor__(self):
        self.bus.close()
        return

    def get_number(self):
        data            = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number          = (upper_data_byte << 6) | (lower_data_byte >> 2)

        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte}, Число: {number}")

        return number

    def get_voltage(self):
        number  = self.get_number()
        voltage = number / 256 * self.dynamic_range
        return voltage 


if __name__ == "__main__":
    try:
        mcp = MCP3021(3.296)
        
        while True:
            voltage = mcp.get_voltage()
            print(f"Current voltage: {voltage}")
            time.sleep(1)


    except KeyboardInterrupt:
        print("ENDNNDNDN")


    finally:
        mcp.__dtor__()