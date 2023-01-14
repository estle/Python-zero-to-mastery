class Person(object):
    def __init__(self):
	    self.gender = "unknown"

    def getGender(self):
	    print(self.gender)

class Male(Person):
    def __init__(self):
	    self.gender = "Male"

class Female(Person):
    def __init__(self):
	    self.gender = "Female"

sharon = Female()
doug = Male()
sharon.getGender()
doug.getGender()