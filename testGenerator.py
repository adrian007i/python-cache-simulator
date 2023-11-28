import random 

# randomly generate n reads and n writes
def uniqueReads(size):
    output = []
    for i in range(0, size + 1):  
        output.append([f'x_{i}' , random.randint(0,100) ]) 

    for i in range(0, size): 
        output.append([f'x_{ random.randint(0, size - 1) }'])  
    return output 