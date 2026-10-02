# Set Difference: All the elements of set 'a' which are not present in set 'b'
# Symmetric Difference: 

a = {10, 20, 30, 40, 50}
b = {10, 30, 60, 90}

print(" ---To check both the sets set difference---")
print(a.difference(b))
print(b.difference(a))

print("\n")
print(" ---To check both the sets symmetric difference---")
print(a.symmetric_difference(b)) # Here both the results are getting same
print(b.symmetric_difference(a)) # Here both the results are getting same