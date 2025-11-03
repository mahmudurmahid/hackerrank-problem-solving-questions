def cats_and_mouse(x, y, z):
    cat_a_distance = abs(x - z)
    cat_b_distance = abs(y - z)

    if cat_a_distance < cat_b_distance:
        return "Cat A"
    elif cat_b_distance < cat_a_distance:
        return "Cat B"
    else: # cat_a_distance == cat_b_distance
        return "Mouse C"

# alternative solution
def alt_cats_and_mouse(x, y, z):
    pass

x = 2
y = 5
z = 4

result = cats_and_mouse(x, y, z)
print(result)
alt_result = alt_cats_and_mouse
print(alt_result)