# A simple code to find the sum of digits

def sum_of_digits(a_string):
    summation = 0
    b_string = str(a_string)
    for i in range(len(b_string)):
        summation += int(b_string[i])
    return summation

print(sum_of_digits(123))