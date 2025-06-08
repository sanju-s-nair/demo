# Simple program to see if a list is sorted or not

def is_sorted(number_list):
    if number_list == sorted(number_list):
        return True
    else:
        return False
    
print(is_sorted([3,4,5,6,9,10]))