

numbers = ["Python", 10, -20, 2.24, 2025] 

print(" --- To find length of a List--- ")
print(len(numbers))

print("\n")
print(" --- Concatinating List in Python--- ")
numbers2 = ["Ironman", "Dr Strange", "Apple", 15]
numbers3 = numbers + numbers2 
print(numbers3)

print("\n")
print(" --- Append or add new elements in List at the end --- ")
numbers.append(2028)
print(numbers)

print("\n")
print(" --- To Insert new items or elements at specific index or in between list --- ")
numbers3.insert(1, "Data_Structure_Algorithms")
print(numbers3)

print("\n")
print(" --- Remove Elements or items from the list by mention direct value --- ")
numbers3.remove(15)
print(numbers3)

print("\n")
print(" --- Remove Elements or items from the list using pop by mention index value--- ")
numbers3.pop(2)
numbers3.pop() # It removed the last element. 
print(numbers3)

print("\n")
print(" --- Remove Elements or items from the list using 'del' and we can delete multiple values with del--- ")
print("Befor deleting elements: ", numbers3)
del numbers3[3]
print(numbers3)

print("\n")
print(" --- We can add multiple elements in list using extend--- ")
print("Befor deleting elements: ", numbers3)
numbers3.extend(["java", "SQL"])
print(numbers3)

print("\n")
print(" --- If we want to clear whole list --- ")
print("Before Clear the list 'numbers' ",numbers)
numbers.clear()
print("After clear the list numbers: ",numbers)

print("\n")
print(" ---- We can combine two lists with other lists--- ")
figures = [1,2,3,4]
alpha = ["a","b","c","d"]

combine = [figures, alpha]
print(combine)
for x in combine:
    print(x)

print("\n")
print(" --- If we want to delete list itself  --- ")
print("Before delete of list numbers: ",numbers)
del numbers
print(numbers)
