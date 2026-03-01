#Find power of a number (x^n)
def power(x, n):
    result=1
    for i in range(n):
        result *= x 
    return result
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
power_result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {power_result}")


#Count the number of digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10  # Remove the last digit
        count += 1
    return count
number = int(input("Enter a number to count its digits: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is: {digit_count}")

#Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b  # Update a to b and b to the remainder of a divided by b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd_result = gcd(num1, num2)
print(f"The greatest common divisor of {num1} and {num2} is: {gcd_result}")
