fruits = {"apple": 250, "orange": 300, "mango": 50}

# Access values
print(fruits["apple"])
print(fruits.get("apple"))

print("\n--- Keys (loop over dict) ---")
for x in fruits:
    print(x)

print("\n--- Values (loop over dict) ---")
for x in fruits:
    print(fruits[x])

print("\n--- Keys (using .keys()) ---")
for x in fruits.keys():
    print(x)

print("\n--- Values (using .values()) ---")
for x in fruits.values():
    print(x)    

print("\n--- Items (key, value pairs) ---")
for x,y in fruits.items():
    print(x, y)

print("\n--- Items (key, value pairs-only using as x variable) ---")
for x in fruits.items():
    print(x)

print("\n--- (Modifications in Dictionary)  ---")

print("\n--- ( Change the vaule of any key ) ---")
fruits["apple"] = 300
print(fruits)

print("\n--- ( Add New key:vaules in Dictionary ) ---")
fruits["pineapple"] = 350
print(fruits)

print("\n--- ( Removing items in Dictionary ) ---")
fruits.pop("apple")
print(fruits)

print("\n--- ( Removing items in Dictionary using 'del' ) ---")
del fruits["orange"]
print(fruits)

print("\n--- ( Find length of a Dictionary  ) ---")
print(len(fruits))

print("\n--- ( copy Dictionary  ) ---")
copy = fruits.copy()
print(copy)

print("\n--- ( copy Dictionary using 'dict'  ) ---")
copy2 = dict(fruits)
print(copy2)

print("\n--- ( Empty Dictionary ) ---")
fruits.clear()
print(fruits)

print("\n--- ( To Delete Entire Dictionary use 'del' as 'del fruits and print(fruits) for Verification ' ) ---")
