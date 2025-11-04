def day_of_programmer(year):
    # invalid year not between 1700-2700
    if not (1700 <= year <= 2700):
        return "Enter a valid year between 1700-2700" 

    # julian calendar
    if 1700 <= year < 1918:
        if year % 4 == 0:
            calendar_days = 366
        else: # year % 4 != 0
            calendar_days = 365
    # gregorian calendar
    elif 1918 < year <= 2700:
        if year % 400 == 0:
            calendar_days = 366
        elif year % 4 == 0 and year % 100 != 0:
            calendar_days = 366
        else:
            calendar_days = 365
    # special case for year 1918 [skipped feb 1st - 13th to change from Julian to Gregorian]
    else: #year == 1918:
        calendar_days = 352
    
    # date returned
    if calendar_days == 365:
        return f"13.09.{year}"
    elif calendar_days == 366:
        return f"12.09.{year}"
    elif calendar_days == 352:
        return f"26.09.{year}"

year1 = 1600
year2 = 2004

result1 = day_of_programmer(year1)
result2 = day_of_programmer(year2)
print(result1)
print(result2)