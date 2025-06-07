def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None  # Return None if there are fewer than 2 elements
    numbers.sort()
    return numbers[1]
numbers = [10, 5, 25, 67, 32, 89, 2]

second_smallest = find_second_smallest(numbers)

if second_smallest is not None:
    print("The second smallest number in the list is:", second_smallest)
else:
    print("The list doesn't have enough elements to find the second smallest number.")
