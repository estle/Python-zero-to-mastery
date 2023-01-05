# iterable can be: list, dict, tuple, set
# iterated -> one by one check each item in the collection
user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for key, value in user.items():
  print(key, value)
print()
for item in user.values():
  print(item)
print()
for item in user.keys():
  print(item)
