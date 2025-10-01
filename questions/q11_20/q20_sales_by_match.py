def sock_merchant(ar):
    sock_dict = {}
    
    for i in range(len(ar)):
        if ar[i] in sock_dict:
            sock_dict[ar[i]] += 1
        else:
            sock_dict[ar[i]] = 1
    
    total_pairs = 0

    for value in sock_dict.values():
        total_pairs += value // 2
    
    return total_pairs

arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
result = sock_merchant(arr)
print(result)