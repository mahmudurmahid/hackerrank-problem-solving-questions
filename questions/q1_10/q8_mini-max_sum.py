def mini_max_sum(arr):
    max_values = sorted(arr)[-4:]
    min_values = sorted(arr)[:4]

    max_total = sum(max_values)
    min_total = sum(min_values)

    return max_total, min_total

def alt_mini_max_sum(arr):
    ascending_arr = sorted(arr)
    descending_arr = sorted(arr, reverse=True)
    
    max_sum = 0
    min_sum = 0

    for number in range(len(ascending_arr) - 1):
        min_sum += ascending_arr[number]
    
    for number in range(len(descending_arr) - 1):
        max_sum += descending_arr[number]
    
    return max_sum, min_sum


arr = [1, 3, 5, 7, 9]
result = mini_max_sum(arr)
print(result)
alt_result = alt_mini_max_sum(arr)
print(alt_result)