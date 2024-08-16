numbers1 = frozenset([1, 2, 3, 4, 5])
numbers2 = frozenset([2, 3, 4, 5,7])

# Combining both of them using "|" operator
# You can also use union() method
combined = numbers1.difference(numbers2)
print("Combined set:", combined)