def birthday(s, d, m):
    num_combinations = 0

    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            num_combinations += 1
        else: # s[i:i + m] != d
            num_combinations += 0
    
    return num_combinations

# alternative solution
def alt_birthday(s, d, m):
    total = 0

    for number in range(len(s) + m - 1):
        if sum(s[number:number + m]) == d:
            total += 1
    
    return total

s = [2, 2, 1, 3, 2]
d = 4
m = 2
result = birthday(s, d, m)
print(result)
alt_result = alt_birthday(s, d, m)
print(alt_result)