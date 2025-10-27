def page_count(n, p):
    front_page = p // 2
    back_page = (n // 2) - (p // 2)

    if front_page < back_page:
        return front_page
    else:
        return back_page

# alternative solution
def alt_page_count(n, p):
    pass

n1 = 5
p1 = 4
n2 = 6
p2 = 2

result1 = page_count(n1,p1)
result2 = page_count(n2, p2)
print(result1)
print(result2)

alt_result1 = page_count(n1,p1)
alt_result2 = page_count(n2, p2)
print(alt_result1)
print(alt_result2)