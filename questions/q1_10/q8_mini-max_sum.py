def mini_max_sum(arr):
    max_values = sorted(arr)[-4:]
    min_values = sorted(arr)[:4]

    max_total = sum(max_values)
    min_total = sum(min_values)

    return max_total, min_total

arr = [1, 3, 5, 7, 9]
result = mini_max_sum(arr)
print(result)