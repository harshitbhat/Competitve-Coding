def checkEvenOrOdd(n):
    if n & 1 == 0:
        return 'Even'
    return 'Odd'


firstNumber = 125;
secondNumber = 8;
print(f'Number {firstNumber} is : {checkEvenOrOdd(firstNumber)}');
print(f'Number {secondNumber} is : {checkEvenOrOdd(secondNumber)}');
