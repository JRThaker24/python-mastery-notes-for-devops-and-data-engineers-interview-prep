from functools import reduce

# we use Implementation of Lambda using 1.filter, 2. map 3. reduce

#First example of using require to create whole function for one single statement and return one single value.
nums = [1,2,3,4,5,6,7,8,9,10]

def is_even(n):
    return n %2==0 

evens = list(filter(is_even,nums))
print(evens)

#same use with lambda function

evens = list(filter(lambda n: n%2==0 ,nums))
print(evens)

#same example of using map
def dauble(n):
    return n * n  

doubles = list(map(dauble,nums))
print(doubles)
#same with lambds
dub = list(map(lambda n: n * n,nums))
print(dub)

#Using reduce

sum = reduce(lambda a,b : a +b ,dub)
print(sum)