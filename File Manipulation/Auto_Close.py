with open("Demo_File.txt", "r+") as f:
    data = f.read()
    if("chopda" in data.lower()):
        print("Location is already mentioned in the file.")
    print(data)

    