# def average(a,b):
#     return (a+b)/2

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# result = average(num1,num2)
# print(f"The average of {num1} and {num2} is: {result}")

#Type of user defined function
#1. Function without parameters and without return value
def greet():
    print("Hello! Welcome to Python programming.")
greet()

#2. Function with parameters and without return value
def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")
greet("Ganesh")

#3. Function without parameters and with return value
def get_greeting():
    name= input("Enter your name: ")
    return f"Hello {name}! Welcome to Python programming."

greeting_message = get_greeting()
print(greeting_message)

#4. Function with parameters and with return value
def calculate_area(radius):
    import math
    area = math.pi * radius ** 2
    return area 
radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")


