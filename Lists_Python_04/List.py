# List: is an ordered collection in python
# Syntax of List: variable = [item1, item2, item3]
# Examples of List: colors = [red, blue, green]
# Examples of List: Data = ["Python, 2.24, 2025"]

print(" ---Printing of list using for loop--- ")
Data = ["Python", 2.24, 2025]

for x in Data:
    print(x)

# To find out if any of the data is present in list or not using if-else condition.
print("\n")
print(" ---To find out if any of the data is present in list or not using if-else condition-- ")
if 2025 in Data:
    print("Yes Present")
else:
    print("No")