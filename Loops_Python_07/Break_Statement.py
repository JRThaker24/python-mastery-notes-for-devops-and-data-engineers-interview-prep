# Break Statement: is used in python to terminate the loop
# Syntax of break statement is:
# while condition:
#       if true:
#       break
# Statement

# Here in while_loop_break: when inside while loop if first statement condition becomes 'True' then and then only it goes break
# If the first condition statement goes false it will goes to direct last while Statement

while True:
    num = int(input("Enter a number: "))
    if num <= 0:
        break
    print(num)
    print(f"Your number was: {num}")
print(f"Your number was 'Negative': {num} so it becomes 'break' ")    

# Example of 'break' statement in Nested_loop in Example(image)