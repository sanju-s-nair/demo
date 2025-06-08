# to see if a list has duplicates
# Input: [1, 2, 2, 3, 3, 3]

def check_duplicates(number_list):
    freq = {}
    for num in number_list:
        if num in freq:
           freq[num] += 1
           return True
        else:
           freq[num] = 1
    return False

print(check_duplicates([1, 2, 3, 4, 4]))