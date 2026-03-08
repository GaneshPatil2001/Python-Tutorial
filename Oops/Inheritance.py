class Employee:
    def __init__(self,cname):
            self.cname=cname
    def getCName(self):
        return self.cname
class Programmer(Employee):
    def __init__(self,cname,name):
        super().__init__(cname)
        self.name=name
    def show(self):
        print(f"{self.name} work in {self.getCName()}")

p1=Programmer("TCS","Ganesh Patil")
p1.show()

print("Company name : ",p1.getCName())