from functools import reduce

def sum_accumulate(x, y):
    """Accumulate the sum of two numbers."""
    return x + y

def sum_of_range(start, end):
    """Calculate the sum of numbers in a given range using reduce."""

    numbers = range(start, end + 1)
    
    total_sum = reduce(sum_accumulate, numbers)
    
    return total_sum

start = 1
end = 10
print(f"The sum of numbers between {start} and {end} is: {sum_of_range(start, end)}")
