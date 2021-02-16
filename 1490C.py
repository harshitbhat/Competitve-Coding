cubes = {}
def preFill():
    for i in range(1,10000):
        cubes[i**3] = True
T = int(input())
preFill()
while T > 0:
    T = T - 1
    n = int(input())
    isPossible = False
    for i in cubes.keys():
        if (n - i) in cubes.keys():
            isPossible = True
            break
    if isPossible:
        print('YES')
    else:
        print('NO')
