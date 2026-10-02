#Decorators in python: In python everything is an object class, function etc, so we can also assign a function to a variable.
# and invocate using new variable 

print("---Examples of how to pass one function to another function---")
def Hello():
    print("Hello")
a = Hello()


print("---Another Examples of how to pass one function to another function---")

def sum(n):
    return n + 10
def mul(n):
    return n * 10
def func(x,y):
    print(x(y))

func(sum,20)
func(mul,20)