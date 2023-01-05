user = {
  '123': [1,2,3],
  'b': 'hello',
  True: 24,
  'greet': 'twice',
}

# avoid errors, 33 is default value if there is no 'age' in user
print(user.get('age', 33))

# rare way to create dictionary, that's why dict is a keyword
user2 = dict(name='JohnJohn')
print(user2)

# more dict methods: https://www.w3schools.com/python/python_ref_dictionary.asp

