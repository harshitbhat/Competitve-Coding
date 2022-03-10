def swapNumbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print(f'After swapping values are: a = {a} and b = {b}')


a = 10
b = 121
print(f'Before swapping values are: a = {a} and b = {b}')
swapNumbers(a, b)