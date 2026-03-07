class student:
    
    def __init__(arg, name, age):
        arg.name = name            # class attribute
        arg.age = age

    def display(arg):
        print("Name:", arg.name)
        print("Age:", arg.age)

s1 = student("Ganesh", 20)
#s1.display()
student.display(s1)
print("Name by calling:", s1.name)
print("Age by calling:", s1.age)

s1.name="Ganesh Patil"          #Instance attribute can be updated
s1.age=24
print("Updated Name:", s1.name)
print("Updated Age:", s1.age)