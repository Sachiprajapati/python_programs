# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Difference
difference_method = set1.difference(set2)
print("Difference (method):", difference_method)

difference_operator = set1 - set2
print("Difference (operator):", difference_operator)

# Intersection
intersection_method = set1.intersection(set2)
print("Intersection (method):", intersection_method)

intersection_operator = set1 & set2
print("Intersection (operator):", intersection_operator)

# Union
union_method = set1.union(set2)
print("Union (method):", union_method)

union_operator = set1 | set2
print("Union (operator):", union_operator)

# Symmetric Difference
sym_diff_method = set1.symmetric_difference(set2)
print("Symmetric Difference (method):", sym_diff_method)

sym_diff_operator = set1 ^ set2
print("Symmetric Difference (operator):", sym_diff_operator)

# Subset
subset_method = set1.issubset(set2)
print("Is set1 a subset of set2 (method)?:", subset_method)

subset_operator = set1 <= set2
print("Is set1 a subset of set2 (operator)?:", subset_operator)

# Superset
superset_method = set1.issuperset(set2)
print("Is set1 a superset of set2 (method)?:", superset_method)

superset_operator = set1 >= set2
print("Is set1 a superset of set2 (operator)?:", superset_operator)
