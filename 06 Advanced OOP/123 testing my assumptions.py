class test:
    def __init__(self, name='Scroodge'):
        self.name = name

    def run(self):
        return self


# When learning, you Test your Assumptions, you understand the subject more deeply
# Assumption: self is the created object
t1 = test()
print(t1 == t1.run())  # Assumption is correct

# Assumption: test is not the same as t1
print(t1 != test())  # Assumption is correct

t1.name = 'Bucks'
print(t1.name)
