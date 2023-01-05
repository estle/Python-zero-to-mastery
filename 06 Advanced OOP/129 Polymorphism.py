# Polymorphism
class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):  # inherit class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):  # subclass
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        User.attack(self)
        print(f'attacking with arrows: {self.num_arrows} arrows left')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

for char in [wizard1, archer1]:
    char.attack()  # same method of different objects, that gives diff output - Polymorphism

# At the end of the day Encapsulation, Abstraction, Inheritance, Polymorphism organize our code, make it clean
