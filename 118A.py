def isVowel(char):
    if char == 'a' or char == 'o' or char == 'y' or char == 'e' or char == 'u' or char == 'i':
        return True
    else:
        return False


word = input()
word = word.lower()
ans = ''
for i in word:
    if not isVowel(i):
        ans = ans + '.' + i
print(ans)
    