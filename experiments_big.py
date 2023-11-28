from testGenerator import *


test_cases = []
policies = ["LRU" , "LFU", "FIFO"]

# n unique reads n unique writes
ram = 10000
cache = 1000
data_set = uniqueReads(ram) 

for x in policies:
    test_cases.append({
        "name" : "Unique Reads",
        "ram_size" : ram,
        "cache_size" : cache,
        "replace_policy" : x,
        "read_writes": data_set
    })

def tests():
    return test_cases