# Nested_loop: is loop inside a loop in python 

# Syntax of Nested for_loop:
# for var in sequence:
#     for var in sequence:
          #Statements 
    #Statements

# Syntax of Nested while_loop:
# while condition:
#  while condition:
       #Statements
#   #Statements

print(" ---Nested_loop Programme--- ")

i = 1 

while i <= 3:
    print("Outer while_loop Iteration: ", i)
    j = 1
    while j <= 3:
        print("Inner while_loop Iteration: ", j)
        j += 1
    i += 1
    print("---------------------------------")

print("\n")
print(" ---Nested_loop another programme--- ")

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print('*',end= '')
        j += 1
    print()
    i += 1
   