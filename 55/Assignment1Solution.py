from functools import reduce

def factorial_using_reduce(n):
    return reduce(lambda x, y: x * y, [i for i in range(1, n + 1)])

# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial_using_reduce(number)}")
