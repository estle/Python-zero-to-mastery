
class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):  # inherit Parent class User
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
        print(f'attacking with arrows: {self.num_arrows} arrows left')


wizard1 = Wizard('Merlin', 50)
print(isinstance(wizard1, User))  # Wizard is instance of User (подкласс, экземпляр класса)
# wizard1. methods __Y__ are inherited from the base object class
wizard1.__doc__
print(isinstance(wizard1, object))
