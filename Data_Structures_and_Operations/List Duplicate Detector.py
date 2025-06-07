def find_dups(int_list):
    # Create a dictionary to count occurrences of each integer
    count_dict = {}
    
    # Count occurrences
    for num in int_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Create a set for duplicates
    duplicates = {num for num, count in count_dict.items() if count >= 2}
    
    return duplicates

# Example usage:
example_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 2, 9, 9]
dups = find_dups(example_list)
print("Duplicates:", dups)
