# Subset: If every element of any set like 'a' is part of 'b' is called then 'a' is subset of 'b'
#Superset: we can say that set 'a' is a superset of set 'b' If all elements of set 'b' are elements of set 'a'
# Disjoint: If any of the element common between two sets then it return false but in case none of the element common between 
# two sets then it will return true

a = {10, 20, 30, 40}
b = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
c = {110, 120, 130}

print("---To check whether the both sets are subsets to eachother or not---")
print(a.issubset(b))
print(b.issubset(a))

print("\n")
print("---To check whether the both sets are superset to eachother or not---")
print(a.issuperset(b))
print(b.issuperset(a))

print("\n")
print("---To check whether the both sets are Disjoint to eachother or not---")
print(a.isdisjoint(b))
print(b.isdisjoint(c))




