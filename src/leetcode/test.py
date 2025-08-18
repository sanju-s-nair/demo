def longestCommonPrefix(strs):
    if not strs:
        return ""

    temp_prefix = ""
    for index, letter in enumerate(strs[0]):
        for word in strs[1:]:
            if index >= len(word) or word[index] != letter:
                return temp_prefix
        temp_prefix += letter
    return temp_prefix

print(longestCommonPrefix(["flower","flow","flight"]))