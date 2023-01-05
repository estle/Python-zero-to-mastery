# Sets - unordered collection of unique objects

my_set = {1,2,3,4,5,5} # same brackets as dict uses
my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1,2,2,3,4,5,5]
print(list(set(my_list)))

my_set = {1,2,3,4,5,5}
# print(my_set[0]) error, bc it's unordered without indexes
1 in my_set
len(my_set)
list(my_set)
new_set = my_set.copy()
my_set.clear()
print(new_set, my_set)
