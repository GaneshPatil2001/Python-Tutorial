import pyjokes
joke = pyjokes.get_joke()
# print("This is a joke from the pyjokes library:")
print(joke)
#print("Hello World from Modules_Comments_PIP.py")

#problem 1 : To print the following poem in python using print function and triple quotes.

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')

#problem 2 : To convert the above joke into audio using pyttsx3 library.
import pyttsx3
engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()


#problem 3 : To list all the components in the root directory using os library.
import os

# Specify the directory path
path = "/"

# Check if the path exists
if os.path.exists(path):
    print("\nComponents in the directory:\n")
    
    # List all files and folders
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        
        if os.path.isfile(full_path):
            print(f"File    : {item}")
        elif os.path.isdir(full_path):
            print(f"Folder  : {item}")
        else:
            print(f"Other   : {item}")
else:
    print("The specified path does not exist.")
