class Student:
    def __init__(self, name, age):
        self.__name = name      # private instance variable
        self.age = age

    @classmethod
    def showClassName(cls):
        print("From inside showClassName method")
        print("Class name:", cls.__name__)

    def getName(self):
        return self.__name


s1 = Student("Ganesh", 20)

Student("Ishwar", 24).showClassName()

s2 = Student("Shubham", 24)

print("Student name:", s2.getName())

# creating new instance variable (not recommended for private variables)
s2.__name = "Mayur"

print("Modified instance variable:", s2.__name)

# actual private variable remains unchanged
print("Original private variable:", s2.getName())

Student.showClassName()