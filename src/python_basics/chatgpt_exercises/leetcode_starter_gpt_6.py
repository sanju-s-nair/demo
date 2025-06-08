# A simple code to display table of a number

def table_multiplier(number):
    for i in range (1,11):
        print (f"{number} x {i} = {number*i}")
print(table_multiplier(9))