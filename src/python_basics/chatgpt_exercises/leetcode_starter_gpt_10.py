# Count Vowels

def count_vowels(word):
    vowels, consonants = 0,0
    for character in word.lower():
        if character in ['a','e','i','o','u']:
            vowels += 1
        else:
            consonants += 1
    return f"vowels : {vowels}\nconsonants : {consonants}"

print(count_vowels('mississipi'))