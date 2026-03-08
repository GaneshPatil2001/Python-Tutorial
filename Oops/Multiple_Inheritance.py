class Employee:
    def __init__(self,cname):
            self.cname=cname
    def getCName(self):
        return self.cname
class Coder:
    language="Python"
    def getLanguage(self):
        return self.language
    
class Programmer(Employee,Coder):
    def __init__(self,cname,name):
        super().__init__(cname)
        self.name=name
    def show(self):
        print(f"{self.name} work in {self.getCName()} on {self.getLanguage()} language")

p1=Programmer("TCS","Ganesh Patil")
p1.show()

print("Company name : ",p1.getCName())
print("Woring language : ",p1.getLanguage())