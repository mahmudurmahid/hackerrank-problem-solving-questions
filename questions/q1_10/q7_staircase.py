def staircase(n):
    x = 0
    
    while x <= n:
        spaces = " " * (n - x)
        hashes = "#" * x
        print(spaces, hashes)
        x += 1

# alternative solution
def staircase(n):
    y = 1

    while y != (n + 1):
        spaces = " " * (n - y)
        hashes = "#" * y
        print(spaces + hashes)
        y += 1

result = staircase(6)
print(result)
alt_result = staircase(6)
print(alt_result)