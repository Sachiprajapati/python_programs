def remove_even_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers
numbers = [10, 5, 25, 67, 32, 89, 2, 45]
filtered_numbers = remove_even_numbers(numbers)

print("List after removing even numbers:", filtered_numbers)
