from functools import reduce

def max_of_two(x, y):
    """Return the maximum of two numbers."""
    return x if x > y else y

def find_maximum(numbers):
    """Find the maximum value in a list using reduce."""

    return reduce(max_of_two, numbers)

numbers = [3, 5, 7, 2, 8, 10, 6]
print(f"The maximum value in the list is: {find_maximum(numbers)}")
