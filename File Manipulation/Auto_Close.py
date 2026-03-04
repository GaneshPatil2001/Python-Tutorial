with open("Demo_File.txt", "r+") as f:
    data = f.read()
    if("chopda" in data.lower()):
        print("Location is already mentioned in the file.")
    print(data)


# Problem
import random as rd
score = rd.randint(0, 100)
print("Your score is", score)
with open("Score.txt", "r+") as f:
    high_score = f.read()
    if high_score == "":
        high_score = 0
    else:        
        high_score = int(high_score)
        print("The current high score is", high_score)

    if score > high_score:
        f.seek(0)
        f.write(str(score))
        print("Congratulations! You have a new high score of", score)
    else:        print("Your score is", score, "but the high score is", high_score)

