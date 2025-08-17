def romanToInt(s):
    roman_dict = {'I':'1', 'V':'5', 'X':'10', 'L':'50', 'C':'100', 'D':'500', 'M':'1000', 'IV':'4', 'IX':'9', 'XL':'40', 'XC':'90', 'CD':'400', 'CM':'900'}
    #roman_string = ''
    summation = 0
    if s in roman_dict:
        return roman_dict[s]
    for i in range(len(s)):
        summation += int(roman_dict[str(s)[i]])
    return summation
         
            

print(romanToInt('IX'))
            