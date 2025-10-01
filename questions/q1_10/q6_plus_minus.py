def plus_minus(arr):
    positive_int = 0
    negative_int = 0
    zero_int = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive_int += 1
        elif arr[i] < 0:
            negative_int += 1
        else:
            zero_int += 1
    
    total = len(arr)

    positive_fraction = round(positive_int / total, 6)
    negative_fraction = round(negative_int / total, 6)
    zero_fraction = round(zero_int / total, 6)

    return positive_fraction, negative_fraction, zero_fraction

# alternative solution
def alt_plus_minus(arr):
    positive_int = 0
    negative_int = 0
    zero_int = 0

    for i in arr:
        if i > 0:
            positive_int += 1
        elif i < 0:
            negative_int += 1
        else:
            zero_int += 1

    total = len(arr)

    positive_fraction = round(positive_int / total, 6)
    negative_fraction = round(negative_int / total, 6)
    zero_fraction = round(zero_int / total, 6)

    return positive_fraction, negative_fraction, zero_fraction

arr = [-4, 3, -9, 0, 4, 1]
result = plus_minus(arr)
print(result)
alt_result = alt_plus_minus(arr)
print(alt_result)