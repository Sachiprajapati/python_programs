def have_common_member(list1, list2):
    set1 = set(list1)
    for element in list2:
        if element in set1:
            return True
    return False
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

if have_common_member(list1, list2):
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")
