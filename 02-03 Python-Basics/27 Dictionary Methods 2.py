user = {
  '123': [1,2,3],
  'b': 'hello',
  True: 24,
  'greet': 'twice',
}

print('twice' in user)
print(1 in user.keys()) # same thing

print('hello' in user.values())
print(user.items())
user2 = user.copy()
print(user.clear())
print(user)
print(user2, end='\n\n')

print(user2.pop(True))
print(user2, end='\n\n')

print(user2.popitem())
print(user2)
print(user2.update({'c': 'goodbye'}))
print(user2)
