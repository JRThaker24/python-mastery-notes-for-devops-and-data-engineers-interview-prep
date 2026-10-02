# Slicing: with the help of slicing we can get substring or set of require character from the strings, slicing won't affect
# the original strings it will return new strings with require characters 
# To get a slice write string name with this format: string[start Index: End Index] here starting Index value is included in the string and ending 
# Index vaule is exculded in the string.

str = "Python"

print(str[0:3])
print(str[-4:-1])

# Slicing using default vaule
print("\n")
print(" ---Slicing using default vaules--- ")
print(str[:3])
print(str[3:])
