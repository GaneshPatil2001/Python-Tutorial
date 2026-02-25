#Dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, 
# and they have keys and values.

d={}    #Empty dictionary
marks={"Ganesh": 85, "Ishwar": 90, "Shubham": 78, "Mayur": 92}
print(type(marks))
print(marks)  # Output: {'Ganesh': 85, 'Ishwar': 90, 'Shubham': 78, 'Mayur': 92}
print("Ganesh marks: ", marks["Ganesh"])  # Output: 85

print("Ishwar marks: ",marks.get("Ishwar"))  # Output: 90
marks.update({"Ganesh":88})
print("Ganesh marks: ", marks["Ganesh"])  # Output: 88

marks.update({"Mohini":96})
print(marks)
print(marks.keys())  # Output: dict_keys(['Ganesh', 'Ishwar', 'Shubham', 'Mayur', 'Mohini'])
print(marks.values())  # Output: dict_values([88, 90, 78, 92, 96])
print(len(marks))  # Output: 5

print(marks.get("Vishal"))  # Output: None
#print(marks["Vishal"])  # This will raise a KeyError since "Vishal" is not a key in the dictionary

#Problem 1: WAP to create a dictionary o Hindi words with their English meanings and print it.
hindi_english={}
for i in range(5):
    hindi_word=input("Enter the Hindi word: ")
    english_meaning=input("Enter the English meaning: ")
    hindi_english[hindi_word]=english_meaning
print(hindi_english)

