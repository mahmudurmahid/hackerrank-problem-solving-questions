def picking_numbers(a):
    # count = 0
    current_array = []

    # for i in a:
    #     current_array.append(i)
    #     for j in a:
    #         if abs(i - j) <= 1:
    #             current_array.append(j)
    #             print(current_array)
    
    for i, j in enumerate(a):
        current_array.append(a[i])
        if abs(a[i] - j) <= 1:
            current_array.append(j)
            print(current_array)

a1 = [4, 6, 5, 3, 3, 1]
a2 = [1, 2, 2, 3, 1, 2]

result1 = picking_numbers(a1)
# result2 = picking_numbers(a2)