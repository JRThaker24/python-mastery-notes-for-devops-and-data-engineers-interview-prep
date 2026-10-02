# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]


items = ["apple", "banana", "orange", "apple", "mango", "banana", "apple", "kiwi", "pear", "peach"]
fruits = set()
duplicate_found = set()  # Use a set to store duplicates

for i in items:
    if i in fruits:
        duplicate_found.add(i)  # Add the duplicate to the duplicate_found set 
        # Continue checking for other duplicates
    fruits.add(i)    
if not duplicate_found:
    print(f"All items are unique: {items}")
else:
    print(f"Duplicate items found: {duplicate_found}")  # Print all duplicates found


# More efficient way to check for duplicates using a set as counter. 
print("---More efficient way to check for duplicates using a set as counter---")
items = ["apple", "banana", "apple", "apple", "mango", "banana", "apple", "apple", "pear", "peach"]
items2 = ["apple", "banana", "apple"]
duplicates = set()
duplicates2 = set()
duplicates3 = {}
duplicates4 = {}

for item in items:
    if items.count(item) > 1:
        duplicates.add(item)
        duplicates3[item] = items.count(item)  # Store the count of duplicates in a dictionary
if duplicates:
    print(f"Duplicate items found for items: {', '.join(duplicates)}")
    print(f"Counts: {duplicates3}")
else:
    print("All items are unique in items 1.")

for item in items2:
    if items2.count(item) > 1:
        duplicates2.add(item)
        duplicates4[item] = items2.count(item)
if duplicates2:
    print(f"Duplicate items found for items2: {', '.join(duplicates2)}")
    print(f"Counts: {duplicates4}")
else:
    print("All items are unique in items 2.")



    


