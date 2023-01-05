class math():
    def __init__(self, n):
        self.value = n
    def square(self):
        return self.value**2

p = math(int(input()))
print(p.square())