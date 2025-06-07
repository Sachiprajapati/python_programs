direct_set = {1, 2, 3, 4, 5}
print("Directly initialized set:", direct_set)

empty_set = set()
empty_set.add(6)
empty_set.add(7)
empty_set.add(8)
print("Empty set after adding values:", empty_set)

# From a list
list_to_set = set([9, 10, 11, 12])
print("Set initialized from list:", list_to_set)

# From another set
original_set = {13, 14, 15}
new_set_from_set = set(original_set)
print("Set initialized from another set:", new_set_from_set)

# Using range
range_set = set(range(16, 21))
print("Set initialized using range:", range_set)

# Print elements iteratively
print("Elements of direct_set iteratively:")
for elem in direct_set:
    print(elem)

# Check remove and discard functionality
test_set = {22, 23, 24, 25}
print("Original test set:", test_set)

# Using remove
test_set.remove(23)
print("Set after using remove(23):", test_set)

# Using discard
test_set.discard(24)
print("Set after using discard(24):", test_set)

# Using discard on a non-existent element
test_set.discard(30)
print("Set after using discard(30) on non-existent element:", test_set)

# Using remove on a non-existent element (will raise an error)
try:
    test_set.remove(30)
except KeyError as e:
    print(f"Error when trying to remove(30): {e}")
