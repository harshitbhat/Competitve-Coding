
# Better Solution - will take least number of boats - in ques it was given that at most 2 at a time
def numRescueBoats(people,limit):
    ans = 0
    i = 0
    j = len(people) - 1
    people.sort()
    while i <= j:
        remain = limit - people[j]
        while people[i] <= remain and i < j:
            remain -= people[i]
            i += 1
        ans += 1
        if i >= j:
            break
        j -= 1
    return ans

#print(numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10],50))


def numRescueBoats2(people,limit):
    i = 0
    j = len(people) - 1
    people.sort()
    ans = 0
    while i <= j:
        remain = limit - people[j]
        if people[i] <= remain:
            i += 1
        ans += 1
        if i >= j:
            break
        j -= 1
    return ans

print(numRescueBoats2([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10],50))