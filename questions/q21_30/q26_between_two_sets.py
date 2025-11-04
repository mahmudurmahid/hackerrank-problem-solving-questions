import math

def between_two_sets(a, b):
    l = math.lcm(*a) # find LCM of first array
    g = math.gcd(*b) # find GCD of second array
    count = 0

    for i in range(l, g+1, l):
        if (g % i) == 0:
            count += 1
    
    return count

a = [2, 6]
b = [24, 36]

result = between_two_sets(a, b)
print(result)