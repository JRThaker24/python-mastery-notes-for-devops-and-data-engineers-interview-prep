b = 1
while b <= 5:
    print(b)
    if b == 4:
        break
    b += 1
else:
    print("I will be executed")

print("\n")
# function that returns a function (closure)
def make_printer(msg):
    def printer():
        print(msg)
    return printer
p = make_printer("I am a returned function")
p()                # prints: I am a returned function

print("\n", "Another example ")
def make_printer(msg):
        print(msg)
    

p = make_printer("I am a returned function")
#p()                # prints: I am a returned function
print(p)

print("\n")
def first():
     print("Hello")
second = first
second()

print("---Decorator Fucntion-Testing---")
def func():
    print("World", end='')

def decorator(arg):
    def new_func():
        print("Hello ", end='')
        func()
        print("From this Earth", end='')
    return new_func()

decorator(func)
# new = decorator(func)
# print("\n")
# new()
