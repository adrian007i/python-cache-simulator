# for readwrites
# ["a" , 21] represents a write to ram
# ["a"] represents an attempted read from cache

tests = [
    {
        "name" : "Experiment 1 : Suited for LRU",
        "ram_size" : 200,
        "cache_size" : 2,
        "replace_policy" : "LRU",
        "read_writes":[["a",1],["b",2],["c",3],["a"],["b"],["c"],["c"]]
    },
    {
        "name" : "Experiment 2 : Suited for LFU",
        "ram_size" : 200,
        "cache_size" : 2,
        "replace_policy" : "LFU",
        "read_writes":[["a",1],["b",2],["c",3],["a"],["a"],["b"],["c"]]
    },
    {
        "name" : "Experiment 3 : Suited for FIFO",
        "ram_size" : 200,
        "cache_size" : 2,
        "replace_policy" : "FIFO",
        "read_writes":[["a",1],["b",2],["c",3],["a"],["a"],["b"],["c"]]
    }
]