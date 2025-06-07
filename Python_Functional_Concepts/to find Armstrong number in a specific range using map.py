def is_armstrong_number(n):
    """Check if a number is an Armstrong number."""
    digits = str(n)
    num_digits = len(digits)

    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

    return sum_of_powers == n

def find_armstrong_numbers_in_range(start, end):
    """Find all Armstrong numbers in a given range using map."""
    numbers = range(start, end + 1)

    armstrong_check = map(lambda x: x if is_armstrong_number(x) else None, numbers)
    
    armstrong_numbers = list(filter(None, armstrong_check))
    
    return armstrong_numbers

start = 1
end = 10000
print(f"Armstrong numbers between {start} and {end} are: {find_armstrong_numbers_in_range(start, end)}")
