def get_money_spent(keyboards, drives, b):
    total_prices = []
    affordable_options = []

    for n in range(len(keyboards)):
        for m in range(len(drives)):
            total_prices.append(keyboards[n] + drives[m])

    for i in range(len(total_prices)):
        if total_prices[i] <= b:
            affordable_options.append(total_prices[i])
        else: # total_prices[i] >= b
            affordable_options.append(-1)
        
    most_expensive = max(affordable_options)
    
    return most_expensive

# alternative solution
def alt_get_money_spent(keyboards, drives, b):
    pass

b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]
result = get_money_spent(keyboards, drives, b)
print(result)
alt_result = alt_get_money_spent(keyboards, drives, b)
print(alt_result)