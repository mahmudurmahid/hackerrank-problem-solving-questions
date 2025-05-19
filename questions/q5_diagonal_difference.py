def diagonal_difference(arr):
    l_to_r = 0
    r_to_l = 0

    n = len(arr)

    for i in range(n):
        l_to_r += arr[i][i]
        r_to_l += arr[i][n - 1 - i]

    difference = abs(l_to_r - r_to_l)
    return difference

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
result = diagonal_difference(arr)
print(result)