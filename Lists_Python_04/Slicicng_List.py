# With the help of slicing in python we get sublist or set of require elements from list, slicing won't affect the original list
# it will return new list with require elements.
# For slicing in list syntax is: list [starting index: ending index] here the starting index is included in list and ending index will excluded from the list.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[-4:-1])

print(" ---Slicing with default values---")
print(numbers[:4])
print(numbers[3:])

print("\n")
print(" ---Assign or replace elements in list--- ")
numbers[:4] = [-10, -20, -30, -40]
print(numbers)

print("\n")
print(" ---Remove elements from the list--- ")
numbers[:2] = []
print(numbers)

print("\n")
print(" ---Copy of the whole lists--- ")
numbers_copy = numbers[:]
print(" Numbers list copy is:  ", numbers_copy)

print("\n")
print(" ---To clear whole list element--- ")
numbers[:] = []
print(numbers)