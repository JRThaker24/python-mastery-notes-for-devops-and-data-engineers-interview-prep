# Iterators in python used in List, Tuple, Dictionary, Sets
# Iterators in python  Implements two specifc methods
# 1. iter() and 2. next() , they are called as Iterator Protocols 
# iter():- is used to initialise the iterator and returns iterator objects
# next():- is called Iterator over Iterator it returns the next items from the collection of data.

color = ["red", "blue", "green"]

iterator = iter(color)
print(next(iterator))
print(next(iterator))
print(next(iterator))