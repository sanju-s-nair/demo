# A simple program to find the second largest number in the list

def second_largest(number_list):
    new_number_list = []
    popped_value = max(number_list)
    number_list.remove(popped_value)
    new_number_list.extend(number_list)
    #print(new_number_list)
    maximum_value = max(new_number_list)
    return f"{maximum_value} is the second largest number"

print(second_largest([4,5,6,8,9,10]))