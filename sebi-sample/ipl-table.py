n = int(input())

teams = {}

for i in range(n):
    team = input()
    teams[team] = [team, 0, 0]

m = int(input())

for j in range(m):
    match = input()
    match = match.split(' ')

    teamA = match[0]
    teamB = match[2]

    nrrA = float(match[1])
    nrrB = float(match[3])

    if nrrA > nrrB:
        teams[teamA][1] += 2
    elif nrrA < nrrB:
        teams[teamB][1] += 2
    else:
        teams[teamA][1] += 1
        teams[teamB][1] += 1
    

    teams[teamA][2] += nrrA
    teams[teamB][2] += nrrB

valuesList = list(teams.values())

# print(valuesList)

# print('================================================')

# print(sorted(valuesList, key = lambda x: (x[1], x[2]), reverse=True))
# print(sorted(valuesList, key = lambda x: (x[1], -1*x[2]), reverse=True))

valuesList = sorted(valuesList, key= lambda x : (x[1], x[2]), reverse=True)

for team in valuesList:
    print(team[0], team[1], team[2])