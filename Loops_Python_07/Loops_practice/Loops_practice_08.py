# Prime number checker

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print(f"The number {num} is not prime ")
        break
else:
    print("The number is prime")



    