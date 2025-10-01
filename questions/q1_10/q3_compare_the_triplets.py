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

# alternative solution
def alt_compare_triplets(alice, bob):
    alice_score = 0
    bob_score = 0

    for a, b in zip(alice, bob):
        if a > b:
            alice_score += 1
        elif a < b:
            bob_score += 1
    
    return alice_score, bob_score

alice = [1, 2, 3]
bob = [3, 2, 1]

result = compare_triplets(alice, bob)
print(result)
alt_result = compare_triplets(alice, bob)
print(alt_result)