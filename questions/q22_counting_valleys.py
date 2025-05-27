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

steps = 8
path = ["U", "D", "D", "D", "U", "D", "U", "U"]
result = counting_valleys(steps, path)
print(result)