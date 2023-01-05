class PlayerCharacter:
    membership = True

    def __init__(self, name='anon', age=0):  # self refers to PlayerCharacter
        if self.membership:
            self.name = name  # attributes
            self.age = age

    def shout(self, cry):
        print(f'{cry} {self.name}')
        return 'done'

    @classmethod
    def adding_things(cls, num1, num2):  # cls - standard class param
        return cls('Ted', num1 + num2)

    @staticmethod
    def static_adding_things(num1, num2):
        return num1 + num2


# player1 = PlayerCharacter()
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.name)
print(PlayerCharacter.static_adding_things(8, 4))
