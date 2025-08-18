def romanToInt(s):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    #roman_string = ''
    summation = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman_dict:
            summation += roman_dict[s[i:i+2]]
            i += 2
        else:
            summation += roman_dict[s[i]]
            i += 1
    return summation
print(romanToInt('MCMXCIV')) #result is 2216 but expected is 1994
            