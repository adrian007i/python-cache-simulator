from datetime import datetime
from ram import RAM
from cache import CACHE 

# set the ram size and cache size
# 2 means 2 variables can be stored in the cache
# 100 means 100 variables can be stored in the ram
cache_size = 2
ram_size = 200 

# replacement policies options
# LRU , LFU , FIFO
replace_policy = "LRU"

# initialize the ram and cache classes
ram = RAM(ram_size)
cache = CACHE(cache_size, replace_policy) 


# run experiments here
ram.write("a" , 100)
ram.write("b" , 2)
ram.write("c" , 3) 
cache.read("a")
cache.read("b")
cache.read("c")
cache.read("c") 

hits = cache.getHit()
miss = cache.getMiss()
ratio = hits /  (hits + miss)
print(f"Cache Hits      {cache.getHit()}")
print(f"Cache Misses    {cache.getMiss()}")
print(f"Cache Ratio     {ratio}")
