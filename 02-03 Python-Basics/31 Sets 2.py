# Sets - unordered collection of unique objects
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# Venn diagrames
print(my_set.difference(your_set))
# my_set.discard(5)
# print(my_set)
# print(my_set.difference_update(your_set))
# print(my_set)

print(my_set.intersection(your_set), my_set) # the same as & sym
print(my_set.isdisjoint(your_set)) # have nothing in common == interscetion is empty
print(my_set.union(your_set), my_set | your_set)

print(my_set.issubset(your_set)) # inside of your_set?
print(my_set.issuperset(your_set)) # includes your_set?
