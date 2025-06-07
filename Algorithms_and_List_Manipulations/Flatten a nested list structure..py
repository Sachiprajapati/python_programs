def flatten(nested_list):
    flat_list = []
    
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten(element))
        else:
            flat_list.append(element)
    
    return flat_list
list1 = [1, [2, 3], [4, 5, [6, 7]]]
flattened_list = flatten(list1)

print("Flattened list:", flattened_list)
