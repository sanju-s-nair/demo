# A simple prorgram to remove duplicates from a list

def remove_duplicates(number_list):
    # no_duplicate_list = []
    # no_duplicate_list.extend(set(number_list))
    # return no_duplicate_list
    seen = set()
    result = []

    for num in number_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


print(remove_duplicates([1,1,1,2,2,3]))