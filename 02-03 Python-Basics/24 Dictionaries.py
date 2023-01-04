# Dictionary = Hash table = map {Unordered key-value pair}
dictionary = {
  'a': [1,2,3],
  'b': 'hello',
  'x': 24
}

print(dictionary['b'])
# print(dictionary['c']) get KeyError
print(dictionary)
print(dictionary['a'][-1])

my_list = [
  {
    'a': [1,2,3],
    'b': 'hello',
    'x': 24
  },
  {
    'a': [4,5,6],
    'b': 'bye',
    'x': '-> take a look at this struct again <-'
  }
]
print(my_list[0]['a'][-2])
print(my_list[1]['x'])
