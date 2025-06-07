def square(x):
    """Return the square of a number."""
    return x * x

def cube(x):
    """Return the cube of a number."""
    return x * x * x

def apply_functions_on_range(start, end):
    """Apply square and cube functions on each number in the given range."""
    numbers = range(start, end + 1)
    
    results = map(lambda x: (square(x), cube(x)), numbers)
    
    return list(results)

start = 1
end = 5
results = apply_functions_on_range(start, end)

for number, (squared, cubed) in zip(range(start, end + 1), results):
    print(f"Number: {number}, Squared: {squared}, Cubed: {cubed}")
