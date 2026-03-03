f = open("Demo_File.txt", "r+")

data = f.read()
print("Before Writing:")
print(data)

f.write("I am from Chopda city Jalgaon.\n")

f.seek(0)   # Move cursor to beginning

data = f.read()
print("After Writing:")
print(data)

f.close()

