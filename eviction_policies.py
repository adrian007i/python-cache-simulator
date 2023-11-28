from datetime import datetime

# finds the last most used variable and returns its name to be removed
def LRU(cache): 
    oldest_key, oldest_value = next(iter(cache.items()))

    # iterate a the cache to find the variable
    for key, value in cache.items():

        # variable is never used
        if value['last_used'] is None:
            return key
        
        # compare to find the last used variable
        if value["last_used"] < oldest_value["last_used"]:
            oldest_key = key
            oldest_value = value 
    
    return oldest_key

def LFU(cache): 
    oldest_key, oldest_value = next(iter(cache.items()))

    # iterate a the cache to find the variable
    for key, value in cache.items():

        # variable is never used
        if value['usage_count'] == 0:
            return key
        
        # compare to find the last used variable
        if value["usage_count"] < oldest_value["usage_count"]:
            oldest_key = key
            oldest_value = value 
    
    return oldest_key


def FIFO(cache): 
    oldest_key, oldest_value = next(iter(cache.items()))  
    return oldest_key