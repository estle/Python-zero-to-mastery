class Student():
    # define the class parameter "name"
    name = "First Name"
    def __init__(self, name, age):
        # self.name is the instance parameter
        self.name = name
        self.age = age
        
student1 = Student("Mike", 18)
print(Student.name, student1.name, sep='\n')