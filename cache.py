

from eviction_policies import LRU, LFU, FIFO
from datetime import datetime
import time
from ram import RAM


class CACHE:
    cache = {}
    def __init__(self, cache_size, replacement_policy):
        self.cache_size = cache_size
        self.replacement_policy = replacement_policy 
        self.hit = 0
        self.miss = 0  
        CACHE.cache = {}

    # read a value from cache
    def read(self, name):  
        # create a timestamp for the read access
        time = int(datetime.now().timestamp() * 1e5)   

        # check the cache for the value
        if CACHE.cache.get(name) is not None:  
            self.hit = self.hit + 1
            CACHE.cache[name]["usage_count"] =   CACHE.cache[name]["usage_count"] + 1
            CACHE.cache[name]["last_used"] =  time 
            return f"CACHE READ      {name} = {CACHE.cache[name]['value']}"
             

        # fetch the data from ram if not found in cache
        data_from_ram = RAM.ram[name]

        # check to ensure the value was found in main memory 
        if data_from_ram is None:
            return "DATA NOT FOUND IN RAM"
        
        self.miss = self.miss + 1 
        
        text = ""
        # check if the cache is full
        if len(CACHE.cache) == self.cache_size:
            
            key_to_evict = None
            if self.replacement_policy == "LRU":
                key_to_evict = LRU(CACHE.cache) 
            
            elif self.replacement_policy == "LFU":
                key_to_evict = LFU(CACHE.cache)

            elif self.replacement_policy == "FIFO":
                key_to_evict = FIFO(CACHE.cache)

            if key_to_evict in CACHE.cache: 
                CACHE.cache[key_to_evict]["cached_time"] =  None
                del CACHE.cache[key_to_evict]
                text=  f"CACHE EVICTED   {key_to_evict} \n"

        # write data from ram to cache 
        data_from_ram["last_used"] =  time
        data_from_ram["usage_count"] = data_from_ram["usage_count"] + 1
        data_from_ram["cached_time"] = time
        CACHE.cache[name] = data_from_ram

        return f"{text}STORED IN CACHE {name} = {CACHE.cache[name]['value']} \nCACHE READ      {name} = {CACHE.cache[name]['value']}"
    
    def getHit(self):
        return  self.hit
    
    def getMiss(self):
        return  self.miss