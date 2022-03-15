words = []
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    x = input().split()
    words += x
    if x[len(x) - 1] == 'endpara':
        break

words = words[:-1]
words = ''.join(words).upper()

isMissing = True

for ch in alphabets:
    if ch not in words:
        isMissing = False
        print(ch, end=' ')

if isMissing:
    print('NONE')