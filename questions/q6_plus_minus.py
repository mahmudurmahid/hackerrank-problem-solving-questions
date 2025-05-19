def plus_minus(arr):
    positive_int = 0
    negative_int = 0
    zero_int = 0

    total = len(arr)

    for i in range(len(arr)):
        if arr[i] > 0:
            positive_int += 1
        elif arr[i] < 0:
            negative_int += 1
        else:
            zero_int += 1
    
    positive_fraction = positive_int / total
    negative_fraction = negative_int / total
    zero_fraction = zero_int / total

    return positive_fraction, negative_fraction, zero_fraction

arr = [-4, 3, -9, 0, 4, 1]
result = plus_minus(arr)
print(result)