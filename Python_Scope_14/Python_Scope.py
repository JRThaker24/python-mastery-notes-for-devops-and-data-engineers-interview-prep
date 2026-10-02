# Scode in Python is a regoin in python where particular variable define and accessed, scope helps in avoiding name collision in programmer.
# There are four types of scopes in our programme.
# 1. Local scope
# 2. Enclosing scope
# 3. Globol scope
# 4. Built-in-scope

# 1. A Local scope is a region where a variable is define inside a function which only accessible inside a function.
# 2. An Enclosing scope is a region in programme where a variable define in outer fucntion function which is accessible 
# From both outer function and Nested Function.
#3. A Globol scope is the region of the programme where a variable is define outside any function which access from anywhere from the programme.
# 4. Built-in-scope: is a region in the programme where built-in-Functions can b e accessed from anywhere from the programme. without need to define that.


c = 10 # Globol scope.
def function1():
    a =5  # Enclosing scope
    def function2():
        b = 3  # Local scope
        print("a: ", a)
        print("b: ", b)
        print("c: ", c)
    function2()

function1()
print(c) # Built-in-Fucntions # Other examples as print,len,range
#Python resolve names using LEGB rule : Local,Enclosing,Globol,Built-in


# Globol and Nonlocol Keywords
print("---Example of Globol keyword---")
a = 10 # Here a globol variable 'a' is cannot modify in the function, it can access inside the function but it cannot be modified
def func1():
    b = 10 #NonLocal variable in Enclosing scope which is also cannot modified in Nested functions
    def func2():
        global a # So to modified the globol variable we have to use keyword 'globol'
        a = a + 5
        nonlocal b # So to mofified the NonLocal variable we have to add keyword 'nonlocal' in Nested functions
        b += 10
        print("a: ", a)
        print("Modified b as 'NonLocal Variable': ", b)
    func2()

func1()

