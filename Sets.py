# Sets are unordered collections of unique elements. 
# They are mutable, meaning you can add or remove elements from a set after it has been created.
#  Sets are defined using curly braces {} or the built-in set() function.
# Sets do not allow duplicate elements, and they are not indexed,
#  which means you cannot access elements in a set using an index like you can with lists or tuples.

s=set()     #Don't use s ={} because it will create a dictionary not a set
s.add(1)
s.add(2)
s.add(2)  # Duplicate element, will not be added to the set
print(s,type(s))  # Output: {1, 2}

s.remove(1)  # Removes the specified element from the set
print(s)  # Output: {2}
s.discard(3)  # Removes the specified element from the set if it is present, otherwise does nothing
print(s)  # Output: {2}

s2={3,4,5}
s.add(3)
print(s.union(s2))  # Output: {2, 3, 4, 5}
print(s2.intersection(s))  # Output: {3}
print(s2.difference(s))  # Output: {2}
print(s.symmetric_difference(s2))  # Output: {2, 4, 5}

print(len(s.union(s2)))  # Output: 4
print(s2.issubset(s.union(s2)))  # Output: True
print(s.issuperset(s2.intersection(s)))  # Output: True
print(subset := {2, 3}.issubset(s.union(s2)) ) # Output: True

#Problem 1: WAP to input 8 numbers from the user and display all the unique numbers once.
numbers=set()
for i in range(8):
    num=int(input("Enter the number: "))
    numbers.add(num)
print(numbers)
    
