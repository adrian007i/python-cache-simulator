import random 

def randonly_generate_experiment_data(size , unique_reads):
    output = []
    for i in range(0, size + 1):  
        output.append([f'x_{i}' , random.randint(0,100) ]) 

    for i in range(0, size ): 
        output.append([f'x_{ random.randint(0, int(size * unique_reads)) }'])  
    return output 


experiments = []

ram = 100
cache = 2,
uniqueness = .99  # 10 percent will be unique

for i in range (1 , 2): 
    data_set = randonly_generate_experiment_data (ram, uniqueness)  

    for x in ["LRU" , "LFU", "FIFO"]:
        experiments.append({
            "name" : uniqueness,
            "ram_size" : ram,
            "cache_size" : cache,
            "replace_policy" : x,
            "read_writes": data_set
        })

def experiments2():
    return experiments