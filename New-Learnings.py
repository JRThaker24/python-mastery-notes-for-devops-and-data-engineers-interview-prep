# To find square root we use sqrt fucntion in python
import math # or you can use import math as m and also you import sepcifc functions like as: from math import sqrt,pow

s = math.sqrt(25)
print(s)

# floor and ceil
print(math.floor(2.9))
print(math.ceil(2.9))

# power 
print(math.pow(2,3))

###
# swap 2 variables in python 

# first using 'temp' method

a = 5
b = 6

temp = a
a = b
b = temp

print(a)
print(b)

# using formula method or also you can use xor(^) and also we can use a,b=b,a

c = 3
d = 4

c = c + d
d = c - d
c = c - d

print(c)
print(d)

# If we want to pass multiple data in function then we have to use keyword-variable-argument and we have to pass keyword in argument.
# like as person("Jigar", age=28, city="Dwarka", mob=9408009646)

def person(name, **data):
    print(name)
    print(data)

person("Jigar", age=28, city="Dwarka", mob=1234567890)

# If we want to change the global variabe without affecting the local variabel then we have to us globals() function
a = 10
print(id(a))
def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("In func a", a)
    print(id(a))
    globals()['a'] = 15
    print(a)
    print(x)
    print(id(a))

something()   

# Pass List to a function

def count(nums):
    evennumbers = []
    oddnumbers = []
    even = 0
    odd = 0
    for i in nums:
        if i % 2 == 0:
            even += 1
            evennumbers.append(i)

        else:
            odd += 1
            oddnumbers.append(i)
    return even,odd,evennumbers,oddnumbers


nums = [10,11,12,13,14,15,16,17,18,19,20,21]

even,odd,evennumbers,oddnumbers = count(nums)

print(f"numbers even numbers are {even}, odd numbers are {odd}")
print(f"even numbers are {evennumbers}, odd numbers are{oddnumbers}")

# Print fibonnaci numbers 
def fibo(n):
    h = 0
    j = 1
    if n == 0 or n == 1:
        print(h)
    elif n <0:
        print("Number is negative")
    else:
        print(h)
        print(j)
        for i in range(2,n):
            l = h + j
            if l >= 90:
                break
            h = j
            j = l
            print(l)
            
fibo(5)

#Prime number is a number which is only divisible by 1 and itself.
num = 2
for i in range(2,num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")








