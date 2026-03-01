'''Recursion is a programming technique where a function calls itself in order to solve a problem.
 It typically involves a base case that stops the recursion and a recursive case that breaks  
 the problem into smaller subproblems. Here's an example of a recursive function to calculate
  the factorial of a number:'''

def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# Example usage
number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")

'''Another example of recursion is the Fibonacci sequence, where 
each number is the sum of the two preceding ones.'''
def fibonacci(n):
    if n <= 0:  # Base case: Fibonacci of 0 is 0
        return 0
    elif n == 1:  # Base case: Fibonacci of 1 is 1
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example usage
n = int(input("Enter the position in the Fibonacci sequence: "))
fib_number = fibonacci(n)
print(f"The {n}th Fibonacci number is: {fib_number}")