# Else Class on loops: we use this when for_loop is exhaust and when conditions of while_loop becomes false

print("---Examples of Else class on loop using for_loop----")

num = [10, 20, 30, 40]
for x in num:
    if 50 in num:
        print("I will not be executed")
else:
    print("I will be executed")

print("\n")
print("---Examples of Else class on loop using for_loops_with_break----")
for x in num:
    print(x)
    if x == 20:
        break
else:
    print("I will be executed")

print("\n")
print("---Examples of Else class on loop using while_loops----")

a = 1
while a <= 5:
    print(a)
    a += 1
else:
    print("I will be executed")

print("\n")
print("---Examples of Else class on loop using while_loops_with_break----")

b = 1
while b <= 5:
    print(b)
    b += 1
    if b == 4:
        break
else:
    print("I will be executed")

print("\n")
print(" ---Another Examples of Else class on loop---")

num2 = [2, 4, 6]
num3 = [3,5,9]
for x in num3:
    if x % 2 == 1:
        print("All are odd")
        break
else:
    print("All are even")

