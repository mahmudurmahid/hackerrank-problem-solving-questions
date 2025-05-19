def compare_triplets(a, b):
    a_score = 0
    b_score = 0

    for i, j in zip(a, b):
        if i > j:
            a_score += 1
        elif i < j:
            b_score += 1
        else: # i == j
            a_score = a_score
            b_score = b_score
    
    final_score = [a_score, b_score]
    return final_score

alice = [1, 2, 3]
bob = [3, 2, 1]
result = compare_triplets(alice, bob)
print(result)