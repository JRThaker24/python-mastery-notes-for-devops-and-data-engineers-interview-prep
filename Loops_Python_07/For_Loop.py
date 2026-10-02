# Loop Condition: allow us to execute a block of code repeteadly while the given condition is true 
# when the condition is false it will stop executing the statements

# In Python we have two types of loops
# 1. for_loop
# 2. while_loop

# for_loop: can be used in python to iterate any sequence like string,list, tuple, Dictionary 
# Syntax of for loop is
# for iterating_variable in any_sequence:
                        # statements

str = "Python"
print(" ---for_loop_in_python as in 'string' --- ")
for char in str:
    print(char)

data = ["Python", 10, 2.24, 2025, "Apple"]
print(" ---for_loop_in_python as in 'list' ")
for x in data:
    print(x)

