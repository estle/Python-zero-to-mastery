
class User():
    def sign_in(self):
        print('logged in')


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
        print(f'attacking with arrows: {self.num_arrows} arrows left')


wizard1 = Wizard('Merlin', 50)
archer1 = Wizard('Robin', 200)
# Both share the same method,
print(wizard1.sign_in())
print(archer1.sign_in())
wizard1.attack()
archer1.attack()
