def breaking_records(scores):
    max_score = scores[0]
    min_score = scores[0]

    max_broken = 0
    min_broken = 0

    for i in scores:
        if i > max_score:
            max_score = i
            max_broken += 1
        elif i < min_score:
            min_score = i
            min_broken += 1
        else:
            max_score = max_score
            min_score = min_score
    
    score_record = (max_broken, min_broken)
    return score_record

scores_arr = [12, 24, 10, 24]
scores_arr2 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

result = breaking_records(scores_arr)
print(result)
result2 = breaking_records(scores_arr2)
print(result2)