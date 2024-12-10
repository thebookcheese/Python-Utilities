import random
import time

PipInstalled = False
Sentences = ["Installing Package: ", "Hacking World Governments", "Stealing", "Exporting File:", 'Deleting File', 'Pip Installing']
Sentences2 = ["'s Personal info"]
StealingThings = ['Bank Details', 'Address','Passwords']
Packages = ["HacketyHack", "Random","Pip","HOI4","Totally not virus"]
PersonNames = ["John", "Dan", "Peter","Joe"]
Files = ["Sys32","Passwords","SecretSecret", 'HAHA']
PipPackages = ['Tkinter', 'Matplotlib']
InstalledPipPackages = []

for i in range(50):
    time.sleep(random.uniform(0.1,0.15))
    Sentence = random.randint(0, len(Sentences))
    if Sentence == 3:
        ThingToSteal = StealingThings[random.randint(0, len(StealingThings)-1)]
        Person = PersonNames[random.randint(0,len(PersonNames)-1)]
        print(Sentences[2], Person + "'s " + ThingToSteal)
    elif Sentence == 0:
        print(Sentences[1])
    elif Sentence == 2:
        LengthOfPackages = len(Files) - 1
        PackPick = random.randint(0,LengthOfPackages)
        print(Sentences[2], Files[PackPick])
    elif Sentence == 1:
        File = Packages[random.randint(0, len(Files)-1)]
        if File == "Pip" and PipInstalled == True:
            print("Pip Already Installed")
        else:
            PipInstalled = True
            print(Sentences[0],File)
    elif Sentence == 4:
        print(Sentences[4], Files[random.randint(0,len(Files)-1)])
    elif Sentence == 5:
        if PipInstalled == True:
            PipPackage = PipPackages[random.randint(0, len(PipPackages) - 1)]
            if PipPackage in InstalledPipPackages:
                print(f"{PipPackage} already installed")
            else:
                InstalledPipPackages.append(PipPackage)
                print(Sentences[2], PipPackage)
    else:
        RandomPersonName = random.randint(0,(len(PersonNames)-1))
        print(Sentences[2], PersonNames[RandomPersonName],Sentences2[0])