def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Driver Code
targetNumber = 5
result = factorial(targetNumber)
print("The factorial of " + str(targetNumber) + " is: " + str(result))