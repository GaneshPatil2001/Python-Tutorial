class student:
    def __init__(self,__name__, age):
        self.__name__=__name__
        self.age=age
    
    @staticmethod
    def display():
        print("hii")
    
    def _showName_(self):
        print("From inside showname method")
        print(self.__name__)

s1=student("Ganesh",20)

s1.display()

student("Prashant",21).display()

student("Ishwar",24)._showName_()

s2=student("Shubham",24)
print("Use class attribute here",s2.__name__)
s2.__name__="Mayur"       #Instance variable is created
print("Now modification within instance variable : ",s2.__name__)