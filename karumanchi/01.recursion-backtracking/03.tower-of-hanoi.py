def towerOfHanoi(numberOfDisks, start = 1, end = 3):
    if numberOfDisks:
        towerOfHanoi(numberOfDisks - 1, start, 6 - start - end)
        print(f'Move disk {numberOfDisks} from {start} to {end}')
        towerOfHanoi(numberOfDisks - 1, 6 - start - end, end)


towerOfHanoi(3)
