# check if the words are anagrams

# Input: "listen", "silent"
# Output: True

def anagram_test(word, anagram_word):
    freq = {}
    anagram_freq = {}
    if len(word) == len(anagram_word):
        for characters in word:
            if characters in freq:
                freq[characters] += 1
            else:
                freq[characters] = 1

        for characters in anagram_word:
            if characters in anagram_freq:
                anagram_freq[characters] += 1
            else:
                anagram_freq[characters] = 1
        
        if freq == anagram_freq:
            return f"The words {word} and {anagram_word} are anagrams"
        else:
            return f"The words {word} and {anagram_word} are not anagrams"
        
    else:
        return f"The words {word} and {anagram_word} are not anagrams"
    

print(anagram_test('nomed','demon'))

#alternate method by gpt
# from collections import Counter

# def anagram_test(word, anagram_word):
#     if len(word) != len(anagram_word):
#         return f"The words {word} and {anagram_word} are not anagrams"
    
#     if Counter(word) == Counter(anagram_word):
#         return f"The words {word} and {anagram_word} are anagrams"
#     else:
#         return f"The words {word} and {anagram_word} are not anagrams"

# print(anagram_test('nomed', 'demon'))

