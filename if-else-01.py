#python programme Odd/Even

num = int(input("Enter a number: "))

if num/2 == 0:
    print("Even")
else:
    print("Odd")

#List Method Programme 


numbers = [10, 20, 30, 40, 50]
#Write your code here

num = int(input(""))
num2 = int(input("")) 

if 0 <= num:
    numbers.insert(num,num2)
    print(numbers)
else:
    print("invalid")    

# index replace in python 

numbers = [10, 20, 30, 40, 50]
#Write your code here

num = int(input(""))
num2 = int(input("")) 

if 0 <= num:
    numbers[num] = num2
    print(numbers)
else:
    print("invalid")  


# Tuple count 

data = (10, 20, 100, 300, 10, 35, 67, 10, 10)
print(data.count(10))
print(data.index(20))

