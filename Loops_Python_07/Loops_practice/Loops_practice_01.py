# Counting Positive Numbers
#Problem: Given a list of numbers, count how many are positive.
#numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_count = 0
sum_of_positive_numbers = 0

for i in numbers:
    if i >0:
        positive_count += 1
        sum_of_positive_numbers += i
print(f"Positive Numbers are {positive_count}")
print(f"Sum of Positive Numbers is {sum_of_positive_numbers}")
