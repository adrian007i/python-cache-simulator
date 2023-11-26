# this class simulates the main memory (ram) in computing.
# user inputs are first stored in ram
# when the user wants to read a value, it is moved from ram to cache

class RAM:
    ram =  {}

    def __init__(self, ram_size):
        self.ram = ram_size
        RAM.ram = {}

    # write the variable to ram dictionary
    def write(self, name, value):
        data_packet = {"value": value, "last_used": None, "usage_count": 0}

        # check if value exist, if it exist, we update
        if RAM.ram.get(name) is not None:
            RAM.ram[name] = data_packet
            return f"{name} UPDATE IN RAM"

        # ensure ram still has space
        if len(RAM.ram) == self.ram:
            return "RAM FULL"

        # store the packet in ram
        RAM.ram[name] = data_packet
        return f"STORED IN RAM   {name} = {value} "