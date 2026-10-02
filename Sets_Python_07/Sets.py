# 'Sets' in python 

print("--- Sets in python --- ")
print("\n A Sets can be define as Unorderd collection with no duplicate items and Sets are Unindexed and not support Indexing")

data = {10, 20, 30 ,40, 50, 10, 20, 50}
print("\n",data)

print("\n--- ( Present Sets vaules using for loop ) ---")
for x in data:
    print(x)

print("\n--- ( Checks if the vaule is present in Sets or not using If-else condition ) ---")
if 20 in data:
    print("Yes")
else :
    print("No")    

