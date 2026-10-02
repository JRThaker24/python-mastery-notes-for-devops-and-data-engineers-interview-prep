# when function execution reaches to the 'return' statement it terminates the execution of the function and return to the calling fucntion
print("---Examples of Return Functions---")
def func():
    print(5)
    return 10

a = func
print(a())



print("\n")
print("---Another Examples of Return Functions---")
def func2():
    return 10,20

b,c = func2()
print(f"Here b = {b}, Here c = {c}")

print("\n")
print("---Another Examples of Return Functions---")

def func3(x,y):
    return x == y
    print("I won't be executed")

func3(10, 10)
d = func3(10, 10)
 # print(d)

f = func3(10, 5)
print(f)
d = func3(10, 6)
print(d)

print("\n")
def func4(x,y):
    if x == y:
        print("same")
        return 5
    else:
       print("Not same")
       return 10 

    

func4(2,3)
e =  func4(2,3)
print(e)
g = func4(10, 10)
print(g) 

# here in func4 function case even we not assign any variable and func4(2,3) it automatically calls and and also if we assign variable
# like e = func4(2,3) so it also again call and also func4(10, 10) it automatically calls so why it such not happen in case of func3 when
# i write d = func3(10, 10) it not call automatically and also i when i direct call it without variable like func3(10, 10) it doesn't calls automatically