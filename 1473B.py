def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return int((a/gcd(a,b)) * b)
T = int(input())
while T > 0:
    T = T - 1
    s = input()
    t = input()
    lcmOfString = lcm(len(s),len(t))
    s = s * int(lcmOfString/len(s))
    t = t * int(lcmOfString/len(t))
    if s == t:
        print(s)
    else:
        print(-1)