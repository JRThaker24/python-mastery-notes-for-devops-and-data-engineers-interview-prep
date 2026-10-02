import time

def timer(func):
    def calculation(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f" {func.__name__} ran in start-time: {start_time:.2f} and total-time: {end_time:.2f} seconds, execution time: {end_time - start_time:.2f} seconds")
        return result
    return calculation

@timer
def new_func(n):
    time.sleep(n)

new_func(3)
