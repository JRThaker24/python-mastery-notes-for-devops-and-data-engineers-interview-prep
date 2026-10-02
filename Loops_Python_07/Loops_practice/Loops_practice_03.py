# Multiplication Table Printer
#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter a number: "))

for i in range(1,11):
    if i == 5:
        continue
    print(f"Multiplication of {num} * {i} = ", num * i)

# Reverse a String
# Problem: Reverse a string using a loop.   
    



