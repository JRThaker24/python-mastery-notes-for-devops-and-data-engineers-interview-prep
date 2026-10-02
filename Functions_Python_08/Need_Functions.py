# Functions in python: we can define a functions in python, Function is a group of statements that together performs a specific tasks 
# Why we need Function:
# Functions 1. improve Modularity and 2. Code resuseability
#
# Imrove Modularity: means if we have a large programme so it becomes very difficult to maintain it if it divides into smaller
# into small seprats module then it very easy to maintain it.also suppose if any error is occuring in our programme then we can 
# easily debug the programme and if particular module is not working then we can test and debug that specific module rather then 
# the entire programme
#
#Code reuseabilty: Suppose if we get two numbers from the users to check whether the given number it is positive or negative 
# so instead of repeating code again we can put the block of code in function and we can call that function whenever we want.
#
#In python to define a function 'def' is used and followed by function_name and '()' paranthesis anf after following four spaces statemets are starts

print(" ---Examples of functions in Python---")
def Hello():
    print("Hello World")

Hello()
print(Hello())


def check(num):
    if num == 0:
        print("The number is neither Positive or negative")
    elif num < 0:
        print("The number is Negative")
    else:
        print("The number is positive")

num = int(input("Enter a number: "))
check(num)
