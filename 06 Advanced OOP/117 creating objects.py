class PlayerCharacter:
    def __init__(self, name, age): # self refers to PlayerCharacter
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Bob', 31)
player2 = PlayerCharacter('Tom', 17)

print(player1.run())
print(player2.name)
print(player1)
print(player2)
