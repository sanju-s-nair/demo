#hash map basics - count the value

# Input: [1, 2, 2, 3, 3, 3]
# Output: {1: 1, 2: 2, 3: 3}

def count_keys(passed_value):
    freq = {}

    for num in passed_value:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

print(count_keys([1, 2, 2, 3, 3, 3]))