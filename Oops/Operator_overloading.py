class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self, other):
        return self.n+other.n
    def __sub__(self, other):
        return other.n/self.n
    def __truediv__(self, other):
        return other.n/self.n
    def __mul__(self, other):
        return other.n*self.n

n= Number(12)
m= Number(36)

print(n+m)
print(n-m)      #Here we use substration for operator overloading but actual o/p is comes after division
print(n*m)
