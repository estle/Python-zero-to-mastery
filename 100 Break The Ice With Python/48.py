class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width
    
rect = Rectangle(2, 4)
print(rect.area())