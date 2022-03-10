def checkSigns(a, b):
    if a ^ b < 0:
        return "Opposite signs"
    return "Same sign"

x = 100 
y = -1
print(f'For inputs {x}, {y} :  {checkSigns(x, y)}')

z = -100 
p = -501
print(f'For inputs {z}, {p} :  {checkSigns(z, p)}')