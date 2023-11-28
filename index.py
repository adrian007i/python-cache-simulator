from datetime import datetime
import time

from ram import RAM
from cache import CACHE 
 

from experiments.summary_experiment import experiments2
from experiments.in_depth_experiment import experiments

with open('result/results_in_depth.txt', 'w') as file: 
    file.close()

# run small experiments in detail here 
for test in experiments:  
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

    with open('result/results_in_depth.txt', 'a') as file:
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

with open('result/results_summary.csv', 'w') as file2:
    file2.write("UNIQUE_READS_PERCENT, POLICY, READ_WRITES, CACHE_SIZE, RAM_SIZE, HIT, MISS, RATIO,TIME ns\n")
    file2.close()

# run small experiments in detail here 
for test in experiments2():  

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


    hits = cache.getHit()
    miss = cache.getMiss()
    ratio = hits /  (hits + miss)

    
    end_time = time.time() 
    with open('result/results_summary.csv', 'a') as file2: 
        file2.write(f'{test["name"]},{test["replace_policy"]}, {len(test["read_writes"])},{test["cache_size"]},{test["ram_size"]},{hits} ,{miss}, {ratio},{(end_time - start_time) * 1000}\n')

    

print("RESULTS SAVED")


