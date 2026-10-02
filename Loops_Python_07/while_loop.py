# while_loop: can used in the situation when we don't know the exact iteration count
# Syntax of while_loop:
# while condition:
     #Statements
# In while_loop first while conditon is check if it true then and then only it goes inside #Statements then if #Statement is true 
# So it finally goes to again while condtion and check while condition again and this loop work like this accordingly

print(" ---while_loop programme ----")
number = int(input(" Enter a number: "))
count = 0

while number > 1:
    number = number >> 1 # num num / 2
    count = count + 1 
print(count)

print("\n")
print(" ---while_loop another programme--- ")

number2 = int(input("Enter a number: "))

while number2 >= 1:
    print(number2)
    number2 = number2 - 1
    
