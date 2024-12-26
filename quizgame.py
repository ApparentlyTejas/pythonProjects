print ("welcome homie")
playing = input("Do ya wanna play? ")
if playing.lower() != "yes":
    quit()
print("okay! lets start")    
score = 0
answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Yessir!")                
    score += 1
else:
    print("Nah fam!")
answer = input("what does gpu stand for? ")
if answer.lower()== "graphics processing unit":
    print("Yessir!")
    score += 1
else:
    print("nah fam")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Yessir!')
    score += 1
else:
    print("Nah fam!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Yessir!')
    score += 1
else:
    print("Nah fam!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")