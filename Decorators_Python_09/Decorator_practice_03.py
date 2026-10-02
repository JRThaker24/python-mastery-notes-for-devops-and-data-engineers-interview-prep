# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, 
# so that when it's called with the same arguments, the cached value is returned instead 
# of re-executing the function.

from functools import wraps
import time

def cache(func):
    cache_values = {} # is set up a dictionary to store the cached values of the function calls based on their arguments.
    print(cache_values)

    @wraps(func)
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args] # here the decorator checks if the arguments passed to the function are already present in the cache_values dictionary. If they are, it returns the cached value instead of executing the function again.
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper
@cache
def new_func(a,b):
    time.sleep(4)
    return a + b

print(new_func(10,20)) 
print(new_func(10,20)) 