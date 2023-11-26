from datetime import datetime
from ram import RAM
from cache import CACHE 
from experiment import tests  
with open('results.txt', 'w') as file: 
    file.close()

# run experiments here 
for test in tests:  
    log = ""

    # initialize the ram and cache classes
    ram = RAM(test["ram_size"])
    cache = CACHE(test["cache_size"] , test["replace_policy"])  # policies are (LRU , LFU , FIFO)  
    
    # iterate inputs and outputs
    for req in test["read_writes"]:
         
        if(len(req) == 2):
            log = log + ram.write(req[0], req[1]) + "\n" #write
        else:   
            log = log + cache.read(req[0]) + "\n" #read

    with open('results.txt', 'a') as file:
        file.write(test["name"])
        file.write("\n---------------------\n")
        file.write(log)
        hits = cache.getHit()
        miss = cache.getMiss()
        ratio = hits /  (hits + miss)
        file.write(f"\nSUMMARY\n")
        file.write(f"Cache Hits      {cache.getHit()} \n")
        file.write(f"Cache Misses    {cache.getMiss()} \n")
        file.write(f"Cache Ratio     {ratio * 100}% \n")
        file.write(f"FINAL CACHE:    ")
        file.write(str(CACHE.cache)) 
        file.write(f"\n\n") 


print("RESULTS SAVED IN results.txt")