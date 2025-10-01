def staircase(n):
    x = 0

    while x <= n:
        spaces = " " * (n - x)
        hashes = "#" * x
        print(spaces, hashes)
        x += 1

result = staircase(6)
print(result)