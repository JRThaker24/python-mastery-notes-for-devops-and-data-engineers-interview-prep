# When a generally Error and Excemption occur Python generally stop and generate error message.
# So using 'try and except' ussually handle those errors 
# So any Error or Exception occurs it will test the code in try if fails excemption will handle if no any error occurs the excemption part will not occur
#
# Syntax:
# try:
    #Statement:
# except:
#    #Statement
#Also with try-except-else
# Syntax:
# try:
#   #Statement
# except:
#   #Statement
# else:
#    #Statement

print("---Examples of try-except-else Condtion---")
def sum(a,b):
    try:
        print(a/b)
    except:
        print("Division is not occur")
    else:
        print("Division occur successfully")

sum(10,5)
sum(10,0)

print("---Example of try-except-finally clause in python---")
def func():
    try:
        x = 10
        print(x)
    except:
        print("Something went wrong")
    finally:
        print("Hello I'am In")
func()

print("--- Another Example of try-except-finally clause in python---")
def func2(a,b):
    try:
        print(a/b)
    except:
        print("Something went wrong")
    finally:
        print("Hello I'am In")        

func2(10,0)


