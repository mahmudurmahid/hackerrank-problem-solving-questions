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

# alternative solution
def alt_sock_merchant(ar):
    sock_dict = {}
    odd_sock_total = 0

    for sock in ar:
        if sock in sock_dict:
            sock_dict[sock] += 1
        else:
            sock_dict[sock] = 1
    
    for value in sock_dict.values():
        if value // 2 != 0:
            odd_sock_total += 1
    
    return odd_sock_total

arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
# result = sock_merchant(arr)
# print(result)
alt_result = alt_sock_merchant(arr)
print(alt_result)