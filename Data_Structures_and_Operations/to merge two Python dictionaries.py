# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merging dictionaries using the update() method
merged_dict = dict1.copy()  # Start with a copy of the first dictionary
merged_dict.update(dict2)   # Add the second dictionary

# Print the merged dictionary
print("Merged dictionary:", merged_dict)
