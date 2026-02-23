#Use of input() function to take user input
name = input("Enter your name: ")
age = input("Enter your age: ") 
print(f"Hello {name}, you are {age} years old.")

no1= int(input("Enter first number: "))
no2= int(input("Enter second number: "))
sum = no1 + no2
print(f"The sum of {no1} and {no2} is: {sum}")
#Note: The input() function always returns a string, 
# so we need to convert it to the appropriate data type (like int or float) 
# if we want to perform mathematical operations.

if no1 > no2:
    print(f"{no1} is greater than {no2}")
elif no1 < no2:
    print(f"{no2} is greater than {no1}")
else:
    print(f"{no1} and {no2} are equal")
