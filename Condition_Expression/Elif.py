age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age < 1:
    print("Invalid age entered.")
else:
    print("You are not eligible to vote.")
print("This statement will always be executed.")

#Problem 1: WAP to input 2 numbers from the user and display the greatest number among them.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")
print("This statement will always be executed.")

#Problem 2: WAP to input a number from the user and check if it is positive, negative, or zero.
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")
print("This statement will always be executed.")
