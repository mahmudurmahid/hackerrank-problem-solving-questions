def bon_appetit(bill, k, b):
    total = sum(bill)
    
    b_charged = total // 2
    b_actual = (total - bill[k]) // 2
    overpayment = b_charged - b_actual

    if b == b_actual:
        return "Bon Appetit!"
    else:
        return overpayment

# alternative solution
def alt_bon_appetit(bill, k, b):
    pass

bill = [3, 10, 2, 9]
k = 1
b = 12

result = bon_appetit(bill, k, b)
print(result)
alt_result = alt_bon_appetit(bill, k, b)
print(alt_result)