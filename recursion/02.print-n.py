def printNaturalNumbers(lower, higher):
    if lower > higher:
        return
    
    print(lower)

    printNaturalNumbers(lower + 1, higher)

n = 5

printNaturalNumbers(1, 5)