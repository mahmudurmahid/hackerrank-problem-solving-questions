def page_count(n, p):
    front_page = p // 2
    back_page = (n // 2) - (p // 2)

    if front_page < back_page:
        return front_page
    else:
        return back_page
    
n = 5
p = 4
result = page_count(n,p)
print(result)
alt_n = 6
alt_p = 2
alt_result = page_count(alt_n, alt_p)
print(alt_result)