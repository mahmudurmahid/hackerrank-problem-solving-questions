def divisible_sum_pairs(ar, k):
    num_pairs = 0

    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (i + j) % k == 0:
                num_pairs += 1
            else:
                num_pairs += 0
    
    return num_pairs

arr = [1, 3, 2, 6, 1, 2]
k = 3
result = divisible_sum_pairs(arr, k)
print(result)