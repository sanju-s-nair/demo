def longestCommonPrefix(strs):
    empty_string = ""
    if empty_string in strs:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        temp_prefix = ""
        for index, letters in enumerate(strs[0]):
            for words in strs[1:]:
                if index >= len(words) or words[index] != letters:
                    return temp_prefix
            temp_prefix += letters 
        return temp_prefix

print(longestCommonPrefix(["flower","flow","flight"]))


        