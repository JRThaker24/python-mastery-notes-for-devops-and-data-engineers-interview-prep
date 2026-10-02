# Tuples in python are immutable objects it similar to list but it cannot change once it define
# Syntax of Tuple is: data = (10, 20, 30, 40, 50)

data = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(" ---Tuples items or elements listing using for loop--- ")
for x in data:
    print(x)

print(data[9])

print("\n")
print(" ---To check whether the specic element present in tuple or not usinf if-else condition")
if 100 in data:
    print("Yes Present")
else:
    print("Not Present")

print("\n")
print(" ---Modifying Tuples as only by delting Tuple using 'del' ")
print("Before deleting Tuple data: ", data)
del data


data2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 10)
print("\n")
print(" ---To find total 'length' of a Tuple--- ") 
print(len(data2))

print("\n")
print(" ---To findout how much time the the number '10' is present in Tuple data2--- ")
print(data2.count(10))
print(data2.count(20))
print(data2.count(30))

print("\n")
print(" ---To get particular index of an Tuple element")
print(data2.index(90))






