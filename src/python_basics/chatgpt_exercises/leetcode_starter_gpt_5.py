# Simple code to find factorial of a number

def factorial(number):
    factorial_value = 1
    if number < 0:
        return f"{number} is a negative number"
    elif number == 0 or number == 1:
        return 1
    else:
        for i in range(number,1,-1):
            factorial_value *= i
        return factorial_value
    
print(factorial(9))
