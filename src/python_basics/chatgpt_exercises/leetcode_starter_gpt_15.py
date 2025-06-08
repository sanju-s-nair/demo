# A simple code to find armstrong number

def armstrong_validation(number):
    armstrong_summation = 0
    b_number = str(number)

    for i in range(len(b_number)):
        #armstrong_summation += int(b_number[i]) * int(b_number[i] )* int(b_number[i])
        armstrong_summation += int(b_number[i]) ** 3
    
    if (armstrong_summation == number):
        return "It's an armstrong number!"
    else:
        return "It's not an armstrong number!"
    
print(armstrong_validation(153))
