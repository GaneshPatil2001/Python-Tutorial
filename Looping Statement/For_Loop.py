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

