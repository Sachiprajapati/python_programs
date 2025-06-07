# Function to find multiple items in a tuple
def find_items_in_tuple(my_tuple, items):
    found_items = []
    for item in items:
        if item in my_tuple:
            found_items.append(item)
    return found_items

# Example tuple
my_tuple = (10, 20, 30, 40, 50)

# Items to find
items_to_find = [20, 50, 60]

# Find the items
found_items = find_items_in_tuple(my_tuple, items_to_find)

print(f"Items found in the tuple: {found_items}")
