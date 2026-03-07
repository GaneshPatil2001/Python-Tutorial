class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    @staticmethod
    def display():
        print("hii")

s1=student("Ganesh",20)

s1.display()