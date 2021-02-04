t = int(input())
while t>0:
    t = t-1
    word = input()
    length = len(word)
    if length>10:
        print(f"{word[0]}{length-2}{word[length-1]}")
    else:
        print(word)