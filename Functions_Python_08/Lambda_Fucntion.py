# Lambda Function: In python we did not always create a function using 'def' sometimes we require temporary functions so we can declare anonymous using 
# Lambda keyword
# Syntax: 
# variable = lambda arguments:Expression
# Here arguments can be any number but here only one expression is require

print("---Examples of Lambda functions---")
a = lambda x,y: x+y
print(a(2,3))

print("\n")
print("--- Another Examples of Lambda functions---")
def func(n):
    return lambda x : x ** n

a = func(2)
result = a(3)
print(result)