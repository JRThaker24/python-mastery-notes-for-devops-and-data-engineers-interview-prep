# range()function accepts the integer range(n) and returns the sequence of numbers which is starting from '0'  to 'n-1'
# If we pass range(10) then it will return numbers from: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 which from '0'  to 'n-1'

print(" ---range()fucntion using for loop")
for x in range(10):
    print(x)

print("\n")
print(" ---range()fucntion from specific range using for_loop ----")
for x in range(5,10):
    print(x)

print("\n")
print(" ---range()fucntion from specific range with 'incriment' using for_loop ----")
for x in range(2,10, 2):
    print(x)