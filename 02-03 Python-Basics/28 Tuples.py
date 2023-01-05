# Tuple - immutable lists
my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'z' can't do it
print(5 in my_tuple)
user = {
  'basket': [1,2,3],
  (1,2): 'tuple is immutable',
  'age': 20
}
print(user.items())
print(user[(1,2)])
