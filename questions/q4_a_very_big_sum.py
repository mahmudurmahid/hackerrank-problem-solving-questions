def a_very_big_sum(ar):
    total = 0

    for i in (range(len(ar))):
        total = total + ar[i]
    
    return total

arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
result = a_very_big_sum(arr)
print(result)
