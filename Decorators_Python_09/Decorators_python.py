# Decorators in python: is function which takes another function as argument and add some new functionality into it and returns the decoreted new function

# Sytax of Decorator is:

# def decorator(arg):
#     def new_function():
#         #Statements
#         #Statements
#         arg()
#         #Statements
#     return new_function

print("---Example of Decorator in python---")

def func():
    print("World", end='')

def decorator(func):
    def new_func():
        print("Hello ", end='')
        func()
        print("From this Earth", end='')
        return new_func()

new = decorator(func)
print("\n")
print(new())

print("\n---Decorator Function-Testing---")
def func():
    print("World", end='')

def decorator(arg):
    def new_func():
        print("Hello ", end='')
        arg()
        print(" From this Earth \n", end='')
    return new_func

decorator(func)
# new = decorator(func)
# print("\n")
# new()