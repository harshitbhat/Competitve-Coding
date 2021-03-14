class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2 :
            return True
        if len(s1) != len(s2):
            return False
        diff = 0
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        if diff != 2:
            return False
        a1 = []
        a2 = []
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                a1.append(s1[i])
                a2.append(s2[i])
        a1.sort()
        a2.sort()
        return a1 == a2