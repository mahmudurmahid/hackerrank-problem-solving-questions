def kangaroo(x1, v1, x2, v2):
    k1_landing_spots = [x1]
    k2_landing_spots = [x2]

    k1_num_jumps = 0
    k2_num_jumps = 0

    while k1_num_jumps < 25:
        k1_num_jumps += 1
        k1_distance = k1_landing_spots[-1] + v1
        k1_landing_spots.append(k1_distance)
    
    while k2_num_jumps < 25:
        k2_num_jumps += 1
        k2_distance = k2_landing_spots[-1] + v2
        k2_landing_spots.append(k2_distance)

    for i, j in zip(k1_landing_spots, k2_landing_spots):
        if i == j:
            return "YES"
        # else: # k1_landing_spots[i] != k2_landing_spots[j]
    return "NO" # outside the loop to check for all pairs [not just the first pair]


x1 = 0
v1 = 3
x2 = 4
v2 = 2
result = kangaroo(x1, v1, x2, v2)
print(result)