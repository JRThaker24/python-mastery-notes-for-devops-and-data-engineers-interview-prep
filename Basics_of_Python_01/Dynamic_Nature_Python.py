# In statically type lanuages like C,C++,Java we have to first declare the type of the variable before 
# assigning vaules to it but in python we can define variables at runtime as python is a dynamically typed language


#Id Function: Return identitiy of an object and identity is an intiger and unique constant throughout the life of the object
print("--- Id function Example ---")
a = 10 
print(id(a))

#Identity Operator: is used to check whether the any two objects share the same memory location or not
# so there are two Identity Operator in python 'is' and 'is not' 
# 'is' operator return true if both the objects shares the same memory location and 

print("\n")
print(" --- Example of identity operator('is') --- ")
x = 10
y = 10 

if x is y:
    print("same")
else:
    print("Different")

print("\n")
print(" --- Example of identity operator('is not ') --- ")
x = 10
y = 20 

if x is not y:
    print("Different")
else:
    print("same")    




