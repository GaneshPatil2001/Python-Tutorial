a=1                               #Integer data type
b=2                               #Integer data type
c="Hello Ganesh"                  #String data type
d=False                           #Boolean data type
e=3.14                            #Float data type
f=[1,2,3,4,5]                     #List data type
g=(1,2,3,4,5)                     #Tuple data type
h={"name":"Ganesh","age":24}      #Dictionary data type
i={1,2,3,4,5}                     #Set data type
j=None                            #NoneType data type
k=complex(1,2)                    #Complex data type
l=bytes(5)                        #Bytes data type
m=bytearray(5)                    #Bytearray data type
n=memoryview(bytes(5))            #Memoryview data type   

print("Addition ",a+b)
print(c)
print(d)
print(e)
print(f)
print(g)
print( h.values())
print(i)
print(j)        
print(k)
print(l)
print(m)
print(n)

#Operators in python
_ganesh =78     #Variable name starts with an underscore and is assigned the value 78
_ganesh += 22   #+= is an assignment operator that adds the right operand to the left operand and assigns the result to the left operand.`
print(_ganesh)
print(type(_ganesh))

d= 4>1      #Comparison operator that checks if 4 is greater than 1 and assigns the result (True) to variable d
d= 4==4     #Comparison operator that checks if 4 is equal to 4 and assigns the result (True) to variable d
print(d)

#Logical operators
x = 5
print(x > 3 and x < 10)  # Logical AND operator: True if both conditions are true
print(x > 3 or x < 4)   # Logical OR operator: True if at least one condition is true
print(not(x < 3 or x < 10))  # Logical NOT operator: True if the condition is false

#Bitwise operators
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print(a & b)  # Bitwise AND: 0101 & 0011 = 0001 (1 in decimal)
print(a | b)  # Bitwise OR: 0101 | 0011 = 0111 (7 in decimal)
print(a ^ b)  # Bitwise XOR:    0101 ^ 0011 = 0110 (6 in decimal)
print(~a)     # Bitwise NOT: ~0101 = 1010 (in two's complement, -6 in decimal)
print(a << 1) # Bitwise left shift: 0101 << 1 = 1010 (10 in decimal)
print(a >> 1) # Bitwise right shift: 0101 >> 1 = 0010 (2 in decimal)

#Assignment operators
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15  
x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 12
x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 24
x /= 4  # Equivalent to x = x / 4
print(x)  # Output: 6.0
x //= 2 # Equivalent to x = x // 2 (floor division)
print(x)  # Output: 3.0
x %= 2  # Equivalent to x = x % 2
print(x)  # Output: 1.0 

#Arithmetic operators
a = 10
b = 5
print(a + b)  # Addition: 10 + 3 = 13
print(a - b)  # Subtraction: 10 - 3 = 7
print(a * b)  # Multiplication: 10 * 3 = 30
print(a / b)  # Division: 10 / 3 = 3.333...
print(a // b) # Floor Division: 10 // 3 = 3
print(a % b)  # Modulus: 10 % 3 = 1
print(a ** b) # Exponentiation: 10 ** 3 = 1000  