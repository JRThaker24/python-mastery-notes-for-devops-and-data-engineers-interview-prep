# When we call a function the data pass to that function is called argument

print(" ---Examples of Functions_Arguments---")

def display(day,month,Year): 
    print("The day is : ", day)
    print("The Month is : ", month )
    print("The Year is : ", Year)

def init():
    display(21,"January",2025)

init()

print("\n")
print(" ---Examples of Functions_Arguments with default parameters---")
def display2(day=27, month="July", Year=2022):
    print("The day is : ", day)
    print("The Month is : ", month )
    print("The Year is : ", Year)

display2()
display2(21,1,2015)
display2(day=24,month=11,Year=1998)

print("\n")
print(" ---Examples of Functions_Arbitary_Arguments with parameters---")
#In Arbitary_Arguments all the arguments converted into tuple and and the pass to arg exaples as : def func(*arg):
def display3(*args):
    print(args)
    for x in args:
        print(x)
    return print(x)

display3("Jigar", 24, "November", 1998, 1, 2,3, 4, 5, 6, 7, 8, 9, 10)
print(" ---Examples of Functions_Arbitary_Arguments with parameters with args---")
def display3(*data):
    print(data)
    for x in data:
        print(x)
    return print(x)

display3("Jigar", 24, "November", 1998, 1, 2,3, 4, 5, 6, 7, 8, 9, 10)

print("\n")
print(" ---Another Examples of Functions_Arbitary_Arguments with parameters---")
def func(*data):
    result = 0
    for x in data:
        print(f"Here 'x' is:  , {x} ")
        result += x  
        print(f"Current Result is: {result}") 
    return print("Sum of all elements of data tuple of function: 'func' ",result)
    
func(10, 20, 30, 40, 50)

# Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format
# key: value.






    


    

