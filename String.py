#String is immutable, which means that once a string is created, it cannot be changed.
name = "Ganesh"  # String data type
greeting = "Hello, " + name + "!"  # String concatenation
nameshort = name[-1:-7:-1]  # String slicing
print(nameshort)  # Output: Gan
print(greeting)  # Output: Hello, Ganesh!

#String methods
print("Length of name:", len(name))  # Output: Length of name: 6
print("Uppercase:", name.upper())  # Output: Uppercase: GANESH
print("Lowercase:", name.lower())  # Output: Lowercase: ganesh
print("Is 'Ganesh' in name?", "Ganesh" in name)  # Output: Is 'Ganesh' in name? True
print("Is 'ganesh' in name?", "ganesh" in name)  # Output: Is 'ganesh' in name? False
print("Replace 'Ganesh' with 'Ganesha':", name.replace("Ganesh", "Ganesha"))  # Output: Replace 'Ganesh' with 'Ganesha': Ganesha
print("Split name into list:", name.split())  # Output: Split name into list: ['Ganesh']
print("Find 'esh' in name:", name.find("esh"))  # Output: Find 'esh' in name: 3
print("Count 'a' in name:", name.count("a"))  # Output: Count 'a' in name: 1
print("Is name alphanumeric?", name.isalnum())  # Output: Is name alphanumeric? True
print("Is name alphabetic?", name.isalpha())  # Output: Is name alphabetic? True
print("Is name numeric?", name.isdigit())  # Output: Is name numeric? False
print("Is name whitespace?", name.isspace())  # Output: Is name whitespace? False   
print("Is name title case?", name.istitle())  # Output: Is name title case? True
print("Is name uppercase?", name.isupper())  # Output: Is name uppercase? False
print("Is name lowercase?", name.islower())  # Output: Is name lowercase? False
print("End with 'h'?", name.endswith("h"))  # Output: End with 'h'? True
print("Start with 'G'?", name.startswith("G"))  # Output: Start with
print("Start with 'g'?", name.startswith("g"))  # Output: Start with 'g'? False
print("Strip whitespace:", "  " + name + "  ".strip())  # Output: Strip whitespace: Ganesh