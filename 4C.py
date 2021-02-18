n = int(input())
database = {}
for i in range(n):
    s = input()
    if s not in database.keys():
        print('OK')
        database[s] = 1
    else:
        newEntry = s + str(database[s])
        database[s] += 1
        database[newEntry] = 1
        print(newEntry)
        