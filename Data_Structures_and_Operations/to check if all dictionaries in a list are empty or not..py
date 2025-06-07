# Define a list 'my_list' containing three empty dictionaries
my_list = [{}, {}, {}]

# Define another list 'my_list1' containing dictionaries, one of which has a key-value pair
my_list1 = [{1: 2}, {}, {}]

# Check if all dictionaries in 'my_list' are empty (i.e., contain no key-value pairs)
# The 'not d for d in my_list' generator expression returns 'True' for each empty dictionary, and 'all' checks if they are all 'True'
print(all(not d for d in my_list))

# Check if all dictionaries in 'my_list1' are empty (i.e., contain no key-value pairs)
# The 'not d for d in my_list1' generator expression returns 'True' for the dictionaries that are empty, and 'all' checks if they are all 'True'
print(all(not d for d in my_list1)) 
