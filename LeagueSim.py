import random

FirstNames = ['Mohammed', 'Ali', 'Peter', 'Pierre','George','John','Mina','Mark','Nicolas','Thiago','Daniel','Juan', 'Carlos']
Surnames = ['Petrović','Maríc','Horvat','Anderson','Ivanov','Martin','Leroy','Petit','Schmitd','Olsen','Garcia','López']
TeamsInLeague = ['Arsenal', 'Acenbourough','Bournemouth','Binster','Chelsea','Chesterman','Danelaw','Densmark','Everton','Eggsalad','Fredrikton','Fifth III Town','Gregoric Town','Germanhy','Hartlepool','Houston','Iglooton','Iceland Man']

f = open("Results.txt", "x")
f.close()

f = open("Results.txt", "a")

League = {
    'Arsenal' : {
    },

    'Acenbourough': {

    },
    'Bournemouth': {

    },
    'Binster': {

    },
    'Chelsea' :{

    },
    'Chesterman':{

    },
    'Danlaw': {

    },
    'Densmark': {

    },
    'Everton': {

    },
    'Eggsalad United' : {

    },
    'Fredrikton': {

    },
    'Fifth III Town' : {

    },
    'Gregoric Town': {

    },
    'Germanhy' : {

    },
    'Hartlepool' : {

    },
    'Houston' : {

    },
    'Iglooton' : {

    },
    'Iceland Man': {

    }

}

LeaguePoints = {
    'Arsenal' : 0,
    'Acenbourough': 0,
    'Bournemouth' : 0,
    'Binster' : 0,
    'Chelsea' : 0,
    'Chesterman' : 0,
    'Danelaw' : 0,
    'Densmark' : 0,
    'Everton' : 0,
    'Eggsalad United': 0,
    'Fredrikton' : 0,
    'Fifth III town': 0,
    'Gregoric Town' : 0,
    'Germanhy' : 0,
    'Hartlepool' : 0,
    'Houston' : 0,
    'Iglooton' : 0,
    'Iceland Man': 0

}


def GeneratePlayerNames():
    for key, value in League.items():
        for i in range(20):
            Name = FirstNames[random.randint(0, len(FirstNames)-1)] + " " + Surnames[random.randint(0,len(Surnames)-1)]
            if i == 1:
                League[key][Name] = {'Goals': 0, 'Assists' : 0, 'Shooting' : random.randint(0,30)}
            elif i <= 8:
                League[key][Name] = {'Goals': 0, 'Assists' : 0, 'Shooting' : random.randint(30, i+70)} 
            elif i > 8 and i <= 11:
                League[key][Name] = {'Goals': 0, 'Assists' : 0, 'Shooting' : random.randint(70, 99)}
            else:
                League[key][Name] = {'Goals': 0, 'Assists' : 0, 'Shooting' : random.randint(30, 70)}
            
def Matches(squad1, squad2, squad1name, squad2name):
    T1Starting11 = []
    T1Starting11Shoot = []
    T1Subs = []
    T1SubsShoot = []
    T1AlreadySubbed = []

    T2Starting11 = []
    T2Starting11Shoot = []
    T2Subs = []
    T2SubsShoot = []
    T2AlreadySubbed = []

    count = 0
    for k,v in squad1.items():
        if count >= 11:
            T1Subs.append(k)
            T1SubsShoot.append(v['Shooting'])
        else:
            T1Starting11.append(k)
            T1Starting11Shoot.append(v['Shooting'])
        count = count + 1
    
    count = 0
    for k,v in squad2.items():
        if count >= 11:
            T2Subs.append(k)
            T2SubsShoot.append(v['Shooting'])
        else:
            T2Starting11.append(k)
            T2Starting11Shoot.append(v['Shooting'])
        count = count + 1
        
    GoalsInMatchT1 = []
    GoalsInMatchT2 = []
    for i in range(9):
        for k, v in squad1.items():
            if k in T1Subs:
                continue
            skill = v['Shooting'] / 10 / 2
            if random.randrange(1, 100, 1) <= skill:
                GoalsInMatchT1.append(k)
                League[squad1name][k]['Goals'] = League[squad1name][k]['Goals'] + 1
                #print(k + ' scored for '+ squad1name +' in the '+str((i+1)*10)+'th minute')
            if i >= 6 and k in T1Starting11 and k not in T1AlreadySubbed:
                if random.randint(1,4) == 2:
                    if k in T1AlreadySubbed:
                        continue
                    SubbedOff = T1Starting11.index(k)
                    SubbedOn = T1Subs[random.randint(0, len(T1Subs)-1)]
                    while SubbedOn in T1AlreadySubbed:
                        SubbedOn = T1Subs[random.randint(0, len(T1Subs)-1)]
                    T1Starting11[SubbedOff] = SubbedOn
                    T1Subs[T1Subs.index(SubbedOn)] = SubbedOff
                    T1AlreadySubbed.append(SubbedOff)
                    T1AlreadySubbed.append(SubbedOn)
                    #print(f"{SubbedOn} has been substituted on for {k} in the {(i+1) *10}th minute")
        for k,v in squad2.items():
            if k in T2Subs:
                continue
            skill = v['Shooting'] / 10 / 2
            if random.randrange(1, 100, 1) <= skill:
                GoalsInMatchT2.append(k)
                League[squad2name][k]['Goals'] = League[squad2name][k]['Goals'] + 1
                #print(k + ' scored for ' + squad2name + ' in the '+str(((i+1)*10))+'th minute')
            if i >= 6 and k not in T2AlreadySubbed and k in T2Starting11:
                if random.randint(1,4) == 2:
                    if k in T2AlreadySubbed:
                        continue
                    SubbedOff = T2Starting11.index(k)
                    SubbedOn = T2Subs[random.randint(0, len(T2Subs)-1)]
                    while SubbedOff in T2AlreadySubbed:
                        SubbedOn = T2Subs[random.randint(0, len(T2Subs)-1)]
                    T2Starting11[SubbedOff] = SubbedOn
                    T2Subs[T2Subs.index(SubbedOn)] = SubbedOff
                    T2AlreadySubbed.append(SubbedOff)
                    T2AlreadySubbed.append(SubbedOn)
                    #print(f"{SubbedOn} has been substituted on for {k} in the {(i+1)*10}th minute")
    #print(f"Score is {squad1name} {len(GoalsInMatchT2)} : {len(GoalsInMatchT2)} {squad2name}")
    if len(GoalsInMatchT1) > len(GoalsInMatchT2):
        return 3, 0
    elif len(GoalsInMatchT1) < len(GoalsInMatchT2):
        return 0, 3
    elif len(GoalsInMatchT1) == len(GoalsInMatchT2):
        return 1, 0


GeneratePlayerNames()
SubsPrinted = False
count = 1
for value in League['Chelsea']:
    if count == 12 and SubsPrinted == False:
        print("\nSubs \n")
    print(value + ":")
    print(League['Chelsea'][value])
    count = count + 1

Points = 0

for b in range(20):
    print(b)
    for c in range(20-b):
        if TeamsInLeague[b] == TeamsInLeague[c]:
            continue
        else:
            T1Points, T2Points = Matches(League[TeamsInLeague[b]], League[TeamsInLeague[c]], TeamsInLeague[b], TeamsInLeague[c])
            LeaguePoints[TeamsInLeague[b]] = LeaguePoints[TeamsInLeague[b]] + T1Points
            LeaguePoints[TeamsInLeague[c]] = LeaguePoints[TeamsInLeague[c]] + T2Points
            print(c)

f.write("Name : Points")
for k,v in LeaguePoints.items():
    f.write(f"{k} : {v}")
