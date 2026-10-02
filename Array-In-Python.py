# In array we have all the vaules of the same data type. In python we have list which can store all the values of different data types. 
# But in array we can store only the values of same data type.
# array in python has no fix size we can expand the size of array as per our requirement. 
# In python we have to import array module to use array in python.

import array

vals = array.array('i',[1, 2, 3, 4, 5])
print(vals)
print("It will return the address of first element and number of elements in array")
print(vals.buffer_info()) # it will return the address of first element and number of elements in array
vals.reverse() # it will reverse the array

print(vals)
print("It will return the number of selected elements in array")
print(vals.count(2)) # it will return the number of elements in array

print(vals)
print("It will add the element at the end of array")
vals.append(6) # it will add the element at the end of array

print(vals)
print("It will add the element at the given index")
vals.insert(2, 7) # it will add the element at the given index

print(vals)
print("It will remove the given element from array")
vals.remove(4) # it will remove the given element from array

print(vals)
print("It will remove the element at the given index")
vals.pop(2) # it will remove the element at the given index

print(vals)
print(r"It will update the element at the given index '/n' ")
vals[0] = 9 # it will update the element at the given index

print(vals)
#vals.byteswap() # it will swap the bytes of the array
#print(vals)
vals.extend([8, 9, 10]) # it will add the elements at the end of array
print(vals)
vals.fromlist([11, 12, 13]) # it will add the elements from the list to the array
print(vals)
vals.tolist() # it will convert the array to list
print(vals)
#vals.index(5) # it will return the index of the given element
#print(vals)

newarray = array.array(vals.typecode, (a*a for a in vals)) # it will create a new array with the square of the elements of the given array.
print(newarray)
print("--- ARRAY USING WHILE LOOP ---")
i = 0
while i <len(newarray):
    print(newarray[i])
    i += 1
