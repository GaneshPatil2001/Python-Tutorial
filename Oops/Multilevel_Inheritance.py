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
        print(f"{self.name} work in {self.getCName()} ")

class Project(Programmer):
    def __init__(self, cname, name,pname):
        super().__init__(cname, name)
        self.pname= pname
    def getProjectDetailes(self):    
        print(f"{self.name} work in {self.getCName()} on {self.pname} project ")

p1=Project("TCS","Ganesh Patil","Image Classification")
p1.getProjectDetailes()

print("\nEmployee name : ",p1.name)
print("Company name : ",p1.cname)
print("Project name : ",p1.pname)