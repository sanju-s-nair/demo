# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

def two_sum(number_list, target):
    number_dict = {}

    for index, numbers in enumerate(number_list): #we use enumerate to get value and index of an item
        complement = target - numbers #to find the second pair
        if complement in number_dict: #checking if the pair exists in the dictionary
            return(number_dict[complement], index) #return index of pair and the existing value
        number_dict[numbers] = index #populate dictionary with index value

print(two_sum([2, 7, 11, 15],9))

