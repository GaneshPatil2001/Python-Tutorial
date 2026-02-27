age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:    
    print("You are not eligible to vote.")
print("This statement will always be executed.")

#Problem 1: WAP to input 2 numbers from the user and display the greatest number among them.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")     

print("This statement will always be executed.")

#Problem 2: WAP to input a year from the user and check if it is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("This statement will always be executed.")