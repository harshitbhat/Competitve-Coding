while True:
    cols = int(input())
    if cols == 0:
        break
    s = input()
    rows = int(len(s)/cols)
    mat = []
    i = 0
    switch = 0
    while i < len(s):
        row = []
        if switch % 2 == 0:
            j = i
            while j < i + cols:
                row.append(s[j])
                j = j + 1
            mat.append(row)
        else:
            j = i + cols - 1
            while j >= i:
                row.append(s[j])
                j = j - 1
            mat.append(row)
        i = i + cols
        switch = switch + 1
    for i in range(0,cols):
        for j in range(0,rows):
            print(mat[j][i],end="")
    print()
