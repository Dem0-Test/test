def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
num = 5
print(f"The factorial of {num} is {factorial(num)}")




def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Print first 10 Fibonacci numbers
print(fibonacci(10))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test the function
number = 11
print(f"{number} is a prime number: {is_prime(number)}")


numbers = [1, 2, 3, 4, 5]

# Calculate sum using a loop
total = 0
for num in numbers:
    total += num

print(f"The sum of the numbers is {total}")



# Using a loop to create a list of squares
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)

# Using list comprehension
squares_comprehension = [i ** 2 for i in range(1, 6)]
print(squares_comprehension)


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
number = 7
print(f"{number} is {check_even_odd(number)}")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Test the calculator
print("Addition: ", add(5, 3))
print("Subtraction: ", subtract(5, 3))
print("Multiplication: ", multiply(5, 3))
print("Division: ", divide(5, 3))



def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Test the function
input_string = "Hello, World!"
print(f"Number of vowels in '{input_string}': {count_vowels(input_string)}")


numbers = [10, 20, 4, 45, 99]

# Using the max() function
largest = max(numbers)
print(f"The largest number is {largest}")
