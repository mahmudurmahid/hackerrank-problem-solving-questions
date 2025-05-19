def simple_array_sum(ar):
    total = 0

    for i in range(len(ar)):
        total = total + ar[i]

    return total

arr = [1, 2, 3, 4, 10, 11]
result = simple_array_sum(arr)
print(result)