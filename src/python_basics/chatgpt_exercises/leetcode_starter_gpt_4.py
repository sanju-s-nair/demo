# Simple program to add upto N natural numbers

def sum_of_natural_numbers(n):
    sum = 0
    for numbers in range(1,n+1):
        sum = sum + numbers
    return f"The sum of {n} natural numbers is {sum}"

print(sum_of_natural_numbers(10))