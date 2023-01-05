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

    def check_arrows(self):
        print(f'arrows left: {self.num_arrows}')

    def run(self):
        print('run really fast')


class HybridBorg(Wizard, Archer):  # have all methods
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('borgie', 50, 100)
hb1.sign_in()
hb1.check_arrows()
hb1.attack()
