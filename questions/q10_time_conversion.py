def time_conversion(s):
    hh = int(s[0:2])
    mm = int(s[3:5])
    ss = int(s[6:8])
    meridian = s[8:]

    if meridian == "AM":
        if hh == 12:
            hh = 00
    else: # meridian == "PM"
        if hh != 12:
            hh = hh + 12

    return f"{hh:02}:{mm:02}:{ss:02}"

# alternative solution
def alt_time_conversion(s):
    hh = s[0:2]
    mm = s[3:5]
    ss = s[6:8]
    meridian = s[8:]

    if meridian == "AM":
        if hh == "12":
            hh = "00"
    else: # meridian == "PM"
        if hh != "12":
            hh = str(int(hh) + 12)
    
    return f"{hh}:{mm}:{ss}"


s = "12:05:00PM"
result = time_conversion(s)
print(result)
alt_result = alt_time_conversion(s)
print(alt_result)