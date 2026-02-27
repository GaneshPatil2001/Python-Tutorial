#For Loops are used to iterate over a sequence (like a list, tuple, string, etc.)
#  and execute a block of code for each item in the sequence.
#Syntax
#for variable in sequence:
    #code to execute

#Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

#Example 2: Iterating over a string
print("\nLetters in the word 'Hello':")
for letter in "Hello":
    print(letter)

#Example 3: Using range() to iterate over a sequence of numbers
print("\nSquares of square from 1 to 10:")
for i in range(1,11):
    print(i**2) 

#Example 4: Using for loop with else
print("\nNumbers from 0 to 4:")
for i in range(5):
    print(i)
else:
    print("Loop is finished")   

#Break statement is used to exit the loop prematurely when a certain condition is met.
print("\nFinding the first even number in the list:")
numbers = [1, 3, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        print(f"The first even number is: {num}")
        break
else:    print("No even number found in the list.")

#Continue statement is used to skip the current iteration of the loop and move to the next iteration.
print("\nSkipping odd numbers and printing even numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

#Nested for loops are used to iterate over multiple sequences or to create a loop inside another loop.
print("\nMultiplication table from 1 to 3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a new line after each row of the multiplication table  

#Example 5: Using for loop with a list of dictionaries
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19}
]
print("\nStudent information:")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}")    

#Example 6: Using for loop with enumerate() to get index and value
print("\nEnumerating fruits in the list:")
for index, fruit in enumerate(fruits):
    print(f"Index: {index+1}, Fruit: {fruit}")  

#Pass statement is used as a placeholder for code that will be implemented later. 
# It allows the loop to run without executing any code.  
print("\nUsing pass statement in a for loop:")
for i in range(5):
    if i % 2 == 0:
        pass  # Placeholder for future code to handle even numbers
    else:
        print(f"{i} is an odd number.")
    