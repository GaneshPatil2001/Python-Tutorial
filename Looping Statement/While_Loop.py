#while loop is used to execute a block of code repeatedly as long as a given condition is true.
#Syntax
#while condition:
    #code to execute

#Example 1: Using while loop to print numbers from 1 to 5
print("Numbers from 1 to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1  

#Example 2: Using while loop to calculate the factorial of a number
num= int(input("\nEnter a number to calculate its factorial: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print(f"Factorial is: {factorial}")

#Example 3: Using while loop with else
print("\nCounting down from 5:")
i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("Countdown finished!")
    