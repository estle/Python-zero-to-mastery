class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) # call __init__ method of User class, the class above
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
# print(wizard1.email)
print(wizard1.email)

# introspection - the object methods, that can be called 
print('# introspection'.upper())
print(dir(wizard1))