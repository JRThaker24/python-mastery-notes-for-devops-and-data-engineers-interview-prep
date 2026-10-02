# When continue statement is encounter inside a loop it will skip the next coresponding statements and next iteration begins or reach to the starting of the loop.


print("---Examples of 'continue' in loop---")
for x in range(1,10):
    if x == 3 or  x == 6:
        continue
    print(x)

i = 5

for x in range(1,11):
    print(i * x)
    range =+ 1

