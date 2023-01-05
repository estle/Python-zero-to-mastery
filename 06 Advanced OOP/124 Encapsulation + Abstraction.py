# 4 Pillars of OOP
# ENCAPSULATION
class PlayerCharacter:  # has extra functionality encapsulated in object

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'hi, {self.name}')


player1 = PlayerCharacter('andy', 12)
# player1.speak()

# ABSTRACTION
player1.speak()
print((1, 2, 3, 1).count(1))  # we dont see how .count is implemented
print(len((1, 3, 2, 1)))  # we dont need to know how len() works
player1.name = '111'
# user doesn't see that .speak() is the method, he breaks it by overwriting
player1.speak = 'booo'
print(player1.speak)
