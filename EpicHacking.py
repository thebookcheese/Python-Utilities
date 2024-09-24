import random
import time

Sentences = ["Installing Package: ", "Hacking World Governments", "Stealing", "Exporting File:"]
Sentences2 = ["'s Personal info"]
Packages = ["HacketyHack", "Random","Pip","HOI4","Totally not virus"]
PersonNames = ["John", "Dan", "Peter","Joe"]
Files = ["Sys32","Passwords","SecretSecret"]

for i in range(20):
    time.sleep(0.1)
    Sentence = random.randint(0, len(Sentences))
    if Sentence == 3:
        print(Sentences[1])
    elif Sentence == 2:
        LengthOfPackages = len(Packages) - 1
        PackPick = random.randint(0,LengthOfPackages)
        print(Sentences[0], Packages[PackPick])
    elif Sentence == 1:
        print(Sentences[3],Files[random.randint(0,len(Files)-1)])
    else:
        RandomPersonName = random.randint(0,(len(PersonNames)-1))
        print(Sentences[2], PersonNames[RandomPersonName],Sentences2[0])