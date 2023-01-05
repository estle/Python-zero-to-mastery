# list, set, dict

my_list = {char for char in 'hello'} # set
print(my_list)

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0} # Dictionary comprehensions
print(my_dict)

my_dict2 = {key: key*2 for key in [1, 2, 3]}
print(my_dict2)