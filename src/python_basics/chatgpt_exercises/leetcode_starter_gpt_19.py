#Find First Non-Repeating Character in a String

# Input: "leetcode"
# Output: 'l'

def count_non_repeating(word):
    freq = {}

    for character in word:
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1

    for letter in freq:
        if freq[letter] == 1:
            return letter

print(count_non_repeating('leetcode'))