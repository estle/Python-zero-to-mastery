class American:
    @staticmethod
    def printNationality():
        print("American")
        
class NewYorker(American):
    @staticmethod
    def printCity():
        print("New York")

NewYorker.printNationality()