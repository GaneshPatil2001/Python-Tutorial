#List is a mutable data type, which means that you can 
# change the elements of a list after it has been created. 
# Lists can contain elements of different data types,
#  including strings, integers, floats, and even other lists.
friends=["Ganesh","Ishwar","Shubham","Mayur",12,32,True]  #List data type
print(friends) 
print(friends[0])  # Output: Ganesh
friends[0] = "Ganesha"  # Modifying the first element of the list
print(friends[0])
print(friends[1:4])  # Output: ['Ishwar', 'Shubham', 'Mayur']

#List methods
friends.append("Rahul") #Adds an element to the end of the list
print(friends)  
friends.insert(1, "Suresh") #Inserts an element at a specific index
print(friends)
friends.remove("Suresh") #Removes the first occurrence of a specified value from the list
print(friends)
name=friends.pop(1) #Removes and returns the element at the specified index
print(name)
print(friends)
friends.insert(1, name) 
print(friends)

list1 = [3,1,2]
print(sorted(list1)) 
#print(list1.sort())      #Return none
#list1.sort()
print(list1)

#List comprehension
squares = [x**2 for x in range(1,11)]  # Creates a list of squares from 0 to 9
print(squares)  

#Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row] 
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9] 

#Tuples are similar to lists, but they are immutable,
#   which means that once a tuple is created, it cannot be changed.
#  Tuples are defined using parentheses () instead of square brackets [].
tuple1=(1, 2, 3, "Ganesh", True)  # Tuple data type
print(tuple1)

tuple2=(1,)
print(type(tuple2))
print(tuple2.count(1))  # Output: 1

#Problem 1 : To create a list of fruits and print it.
fruits=[]
for i in range(5):
    fruits.append(input("Enter the fruit name: "))

print(sorted(fruits))

#Problem 2 : To create a tuple of numbers and print the sum of all the numbers in the tuple.
numbers=()
for i in range(5):
    num=int(input("Enter the number: "))
    numbers+=(num,)
print(sum(numbers))

#Problem 3 : count 0 in the list
list1=[0,1,2,3,0,4,5,0]
print(list1.count(0))

