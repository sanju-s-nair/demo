# A Simple code to see if a string is palindrome or not

def palindrome(word):
    reversed_word = word[::-1]
    if word.lower() == reversed_word.lower():
        return "True, its a palindrome"
    else:
        return "False, its not a palindrome"

print(palindrome("malayaLaM"))