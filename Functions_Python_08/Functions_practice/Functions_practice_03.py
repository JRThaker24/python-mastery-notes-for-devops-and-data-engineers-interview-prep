# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_numbers(limit):
    for num in range(2, limit + 1, 2):
        yield num

even_numbers_gen = even_numbers(10)
print(even_numbers(10))  # This will print the generator object
for even in even_numbers_gen:
    print(even)
