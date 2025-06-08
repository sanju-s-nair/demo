# Simple code to see if a number is odd or even

def is_odd_or_even(number):
    if number not in [0]:
        if number%2==0:
            return "Even"
        else:
            return "Odd"
        

print(is_odd_or_even(11))