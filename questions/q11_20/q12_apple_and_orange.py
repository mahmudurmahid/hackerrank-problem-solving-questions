def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_landed = 0
    oranges_landed = 0

    for apple in apples:
        if s <= apple + a <= t:
            apples_landed += 1
        else: # s > apple + a > t
            apples_landed = apples_landed
    
    for orange in oranges:
        if s <= orange + b <= t:
            oranges_landed += 1
        else: # s > orange + b > t
            oranges_landed = oranges_landed
    
    fruit_landed = [apples_landed, oranges_landed]
    return fruit_landed

s = 7
t = 10
a = 4
b = 12
m = 3
n = 3
apples_arr = [2, 3, -4]
oranges_arr = [3, -2, -4]

result = count_apples_and_oranges(s, t, a, b, apples_arr, oranges_arr)
print(result)
alt_result = alt_count_apples_and_oranges(s, t, a, b, apples_arr, oranges_arr)
print(alt_result)