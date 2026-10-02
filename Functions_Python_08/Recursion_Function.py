# Recursion Function: is a function which calling itself 
# Examples as def func(n):
#                func(n-1)

# Basics Rules of Recurstion:
# 1. Function should call itself
# 2. Recursive function should have a base case so it doesn't make any recusive call so that it should't goes into infinite loops
# Examples as def func(n):
#                      if n == 1:
#                       return
#                func(n-1)
# 3. All the Recursive call should align towards the base case
#  Examples as def func(n):
#                      if n == 1 # Here base if n ==1 
#                       return
#                func(n-1)

print("--- Programme of finding factorial using Recursion---")
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

n = 5 # int(input("Enter the number: "))
if n >0:
    a = factorial(n)
    print(a)
# Stack Overflow: In Recursion new functions calls will created in stack overflow memory if our function does not have any base case
#so it will kepp on creating stack memory section and in some point of time recursive functions call overflow the stack memory section
#As it does not have any stopping point also this happens if it does not allign to base case 
# Detail explaination of this programme is in Python(Log2Base2-Images)    
