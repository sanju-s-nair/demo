# Simple program to count the number of odd and evens in a list

def count_odd_even(number_list):
    odd,even = 0,0
    for items in number_list:
        if items == 0  or items < 0 or items == 1:
            pass
        elif items%2==0:
            even += 1
        else:
            odd += 1
    return f"Odd : {odd}\nEven : {even}"

print(count_odd_even([3,4,9,7,1,6,10,22]))
