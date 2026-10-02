n = int(input("Enter a number: "))
a = 0
number_of_even_numbers = 0
for i in range(1, n+1):
    if i % 2 == 0:
        a += i
        number_of_even_numbers += 1
print(f"Sum of even numbers: {a}")
print(f"Number of even numbers: {number_of_even_numbers}")