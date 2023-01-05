class PlayerCharacter:
    # Class Object Attribute, doesn't change
    membership = True

    def __init__(self, name='anon', age=0):  # self refers to PlayerCharacter
        if self.membership:
            self.name = name # attributes
            self.age = age

    def shout(self, cry):
        print(f'{cry} {self.name}') # new formatting
        return 'done'


player1 = PlayerCharacter('Bob', 31)
player2 = PlayerCharacter('Tom', 17)

print(player1.shout('you cool'))
# print(player2.name)
