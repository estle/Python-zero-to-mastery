# Dunder Methods are veery interesting, bc they allow custom modifying of classes
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'boxbox',
            'has_pets': False
        }

    def __str__(self):  # modified Dunder method
        return f'{self.color}'

    def __len__(self):
        return 5

    # def __del__(self):
    #     print('deleted!')

    def __call__(self):
        return ('yes!')

    def __getitem__(self, i):
        return self.my_dict[i]

    def __hash__(self):
        return 4932374179433971704

    def __bool__(self):
        return False

    def __dir__(self):
        return [].__dir__()


action_figure = Toy('red', 0)
print(action_figure.__str__())
# print(str(action_figure)) - same thing as __str__()
print(len(action_figure))  # built-in functions use Dunder Methods
print(str('action_figure'))
# del action_figure
print(action_figure())
print(action_figure['name'])
print(action_figure.__hash__())
# print('baba loves forest'.__hash__())
print(action_figure.__bool__())
print(action_figure.__dir__())
