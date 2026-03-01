#Find power of a number using recursion
def power_recursive(x, n):
    if n == 0:
        return 1  # Base case: any number raised to the power of 0 is 1
    elif n < 0:
        return 1 / power_recursive(x, -n)  # Handle negative exponent
    else:
        return x * power_recursive(x, n - 1)  # Recursive case
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
power_result = power_recursive(base, exponent)
print(f"{base} raised to the power of {exponent} is: {power_result}")

#Count the number of digits in a number using recursion
def count_digits_recursive(num):
    if num == 0:
        return 0  # Base case: no digits in 0
    else:
        return 1 + count_digits_recursive(num // 10)  # Recursive case: remove the last digit
number = int(input("Enter a number to count its digits: "))
digit_count = count_digits_recursive(number)
print(f"The number of digits in {number} is: {digit_count}")

