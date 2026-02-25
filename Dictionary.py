#Dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, 
# and they have keys and values.

marks={"Ganesh": 85, "Ishwar": 90, "Shubham": 78, "Mayur": 92}
print(type(marks))
print(marks)  # Output: {'Ganesh': 85, 'Ishwar': 90, 'Shubham': 78, 'Mayur': 92}
print("Ganesh marks: ", marks["Ganesh"])  # Output: 85

print("Ishwar marks: ",marks.get("Ishwar"))  # Output: 90
marks.update({"Ganesh":88})
print("Ganesh marks: ", marks["Ganesh"])  # Output: 88

marks.update({"Mohini":96})
print(marks)

print(marks.get("Vishal"))  # Output: None
print(marks["Vishal"])  # This will raise a KeyError since "Vishal" is not a key in the dictionary
