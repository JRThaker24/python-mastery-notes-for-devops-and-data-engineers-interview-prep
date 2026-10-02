#Sum of Even Numbers
#Problem: Calculate the sum of even numbers up to a given number n.

num = int(input("Enter the number: "))
sum_of_even_numbers = 0

for i in range(1,num+1):
    if i % 2 == 0:
        sum_of_even_numbers += i
print(f"sum of even numbers is {sum_of_even_numbers}")
    
