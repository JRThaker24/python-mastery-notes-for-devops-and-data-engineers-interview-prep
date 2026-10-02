# We know that sets in python does not support indexing 
data = {10, 20, 10, 30, 20, 40, 50}
for x in data:
    print(x)

print(" ---To add elements or items in 'sets' we can use 'add'  option--- ")
data.add(60)
print("Before adding new elements: ", data)
print(data)

print("\n")
print(" ---To add elements or items in 'sets' using 'Update'  option--- ")
print("Before adding new elements using 'update' option: ", data)
data.update({70, 80, 90})
print(data)

print("\n")
print(" ---Remove any elements from the sets---")
print("Before removing any elements from the set data: ", data)
data.remove(50)
print(data)

print("\n")
print(" ---Remove any elements from the sets using 'discard' Method---")
print(data)
data.discard(90)
print(data)

print("\n")
print(" ---To Empty the set data---")
print(data)
data.clear()
print(data)

print("\n")
print(" ---To Completely delete the set ---")
del data
print(data)