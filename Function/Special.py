# Function with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}! Welcome to Python programming.")
greet()  # Using default parameter
greet("Ishwar")  # Providing an argument

# Function with variable-length arguments
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3, 5, 5,12))
print(sum_numbers(10, 20, 30))
print(sum_numbers())  # No arguments, should return 0
