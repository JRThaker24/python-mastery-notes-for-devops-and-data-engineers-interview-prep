# In Python we have different types of Inheritance 
# 1. Multiple Inheritance: If class c(a,b): Inherits the properties of multiple classes is called multiple classes

print("---Example of Multiple Inheritance ---")

class A:
    def __init__(self, a):
        self.a = a
class B:
    def __init__(self, b):
        self.b = b
class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c
obj = C(30, 40, 50)
print(obj.a,obj.b,obj.c)

# Multilevel Inheritance: If class c(b): and If class b(A): and class c: 
print("\n---Example of Multilevel Inheritance ---")
class A:    
    def __init__(self, a):
        self.a = a
class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b
class C(B): 
    def __init__(self, a, b, c):
        B.__init__(self, a, b)
        self.c = c
obj = C(30, 40, 50)
print(obj.a,obj.b,obj.c)    