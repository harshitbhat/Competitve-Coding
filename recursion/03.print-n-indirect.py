def printNaturalNumbers(lower, higher):
    if lower < higher:
        lower += 1
        helper(lower, higher)
    else:
        return

def helper(lower, higher):
    if lower <= higher:
        lower += 1
        printNaturalNumbers(lower, higher)
    else:
        return

n = 5
printNaturalNumbers(1, 5)