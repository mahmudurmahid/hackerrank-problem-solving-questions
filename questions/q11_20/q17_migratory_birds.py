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
    birds_dict = {}

    for bird in ar:
        if bird in birds_dict:
            birds_dict[bird] += 1
        else:
            birds_dict[bird] = 1
    
    most_seen_bird = 0
    most_seen_bird_sightings = 0

    for key, value in birds_dict.items():
        if value > most_seen_bird:
            most_seen_bird = key
            most_seen_bird_sightings = value
    
    return f"The most seen bird was {most_seen_bird} which was seen {most_seen_bird_sightings} times"

arr = [1, 1, 2, 2, 3, 2]
result = migratory_birds(arr)
print(result)
alt_result = alt_migratory_birds(arr)
print(alt_result)