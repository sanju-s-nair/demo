#Simple program to check leap year

def is_leap_year(year):
    if year%4==0 and year%100==0 and year%400!=0:
        return f"{year} is not a leap year"
    elif year%4==0:
        return f"{year} is a leap year"
    elif year%4==0 and year%100==0 and year%400:
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
    
    
print(is_leap_year(2400))