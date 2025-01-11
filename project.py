print("Welcome to my computer quiz.")

playing = input("Do you want to play?")
score = 0

if playing.lower() != "yes":
    quit()
else:
   print("Okay! Let's play.")

answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Hw many bones are there in human body?")
if answer.lower() == 206:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got" + str(score) + "questions correct!")
print("You got" + str((score) / 4 *100) + " %.")



