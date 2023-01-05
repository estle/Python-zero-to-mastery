class PlayerCharacter:

    def __init__(self, name, age):
        self._name = name  # convention, means _x shouldn't be changed
        self._age = age

    def speak(self):
        print(f'hi, {self._name}')


player1 = PlayerCharacter('andy', 12)
player1.name = '!!!'
player1.speak()
print(player1._name)
