from datetime import datetime
from ram import RAM
from cache import CACHE 
from experiments_big import tests
from experiments_small import small_tests
import time
 

with open('results_small.txt', 'w') as file: 
    file.close()

with open('results_big.csv', 'w') as file2: 
    file2.close()

# run small experiments in detail here 
for test in small_tests:  
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

    with open('results_small.txt', 'a') as file:
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

with open('results_big.csv', 'a') as file2:
    file2.write("Policy, Tests, Cache, RAM, HIT, MISS, RATIO,time (ns)\n")



# run small experiments in detail here 
for test in tests():  

    start_time = time.time()

    # initialize the ram and cache classes
    ram = RAM(test["ram_size"])
    cache = CACHE(test["cache_size"] , test["replace_policy"])  # policies are (LRU , LFU , FIFO)   
        
    # iterate inputs and outputs
    for req in test["read_writes"]:
         
        if(len(req) == 2):
            ram.write(req[0], req[1]) #write
        else:   
            cache.read(req[0]) #read

    
    end_time = time.time()
    with open('results_big.csv', 'a') as file2:
        file2.write(f'{test["replace_policy"]}, {len(test["read_writes"])},{test["cache_size"]},{test["ram_size"]},{cache.getHit()} ,{cache.getMiss()}, {ratio * 100},{(end_time - start_time) * 1000}\n')



print("RESULTS SAVED")


