def migratory_birds(ar):
    birds_dict = {}

    for i in range(len(ar)):
        if ar[i] in birds_dict:
            birds_dict[ar[i]] += 1
        else:
            birds_dict[ar[i]] = 1

    max_bird_count = 0
    max_bird_id = None

    for bird_value in birds_dict:
        if birds_dict[bird_value] > max_bird_count:
            max_bird_count = birds_dict[bird_value]
            max_bird_id = bird_value
        elif birds_dict[bird_value] == max_bird_count: # in case of tie choose lowest bird key in dict
            max_bird_id == min(max_bird_id, bird_value)

    
    return max_bird_id

def alt_migratory_birds(ar):
    pass

arr = [1, 1, 2, 2, 3, 2]
result = migratory_birds(arr)
print(result)
alt_result = alt_migratory_birds(arr)
print(alt_result)