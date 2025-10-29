def counting_valleys(steps, path):
    sea_level = 0
    valley = 0

    for i in range(len(path)):
        if path[i] == "U":
            sea_level += 1
        else: # path[i] == "D"
            sea_level -= 1
        
        if sea_level == 0 and path[i] == "U":
            valley += 1

    return valley

# alternative solution
def alt_counting_valleys(steps, path):
    sea_level = 0
    valley = 0

    for i in path:
        if i == "U":
            sea_level += 1
        else:
            sea_level -= 1
        
        if sea_level == 0 and i == "U":
            valley += 1
    
    return valley

steps1 = 8
path1 = ["U", "D", "D", "D", "U", "D", "U", "U"]
steps2 = 12
path2 = ["D", "D", "U", "U", "D", "D", "U", "D", "U", "U", "U", "D"]

result1 = counting_valleys(steps1, path1)
result2 = counting_valleys(steps2, path2)
print(result1)
print(result2)

alt_result1 = alt_counting_valleys(steps1, path1)
alt_result2 = alt_counting_valleys(steps2, path2)
print(alt_result1)
print(alt_result2)