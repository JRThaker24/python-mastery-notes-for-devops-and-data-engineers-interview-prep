# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function
# is called.

from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v  in kwargs.items())
        print(f"The function name : {func.__name__} and its args values is {args_value} and its kwargs values are {kwargs_value} ")
        result = func(*args, **kwargs)
        return result
    return wrapper

@debug
def new_func(*args, **kwargs):
    print(f"Name: {kwargs.get('name')}, Surname: {kwargs.get('surname')}, Age: {kwargs.get('age')}, Month: {kwargs.get('month')}, Year: {kwargs.get('year')}")

new_func(11, 12, name="Jigar", surname="Thaker", age=24, month=11, year=1998)

print(new_func.__name__)  # Output: new_func


