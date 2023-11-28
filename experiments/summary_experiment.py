import random 

def randonly_generate_experiment_data(size , unique_reads):
    output = []
    for i in range(0, size + 1):  
        output.append([f'x_{i}' , random.randint(0,100) ]) 

    for i in range(0, size ): 
        output.append([f'x_{ random.randint(0, int(size * unique_reads) - 1) }'])  
    return output 

experiments = []
experiments_size = 10

ram = 1000
cache_size = [10,20,30,40,50,60,70,80,90,100]
uniqueness = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]

for u in  uniqueness:
    for s in  cache_size:
        for i in range (1 , experiments_size): 
            data_set = randonly_generate_experiment_data (ram, u)  

            for x in ["LRU" , "LFU", "FIFO"]:
                experiments.append({
                    "name" : str(u * 100),
                    "ram_size" : ram,
                    "cache_size" : s,
                    "replace_policy" : x,
                    "read_writes": data_set
                })
    
def experiments2(): 
    return experiments