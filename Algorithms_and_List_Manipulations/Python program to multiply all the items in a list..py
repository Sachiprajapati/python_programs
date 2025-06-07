def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result
numbers = [2, 3, 4, 5]
product = multiply_list(numbers)
print("The product of all items in the list is:", product)
