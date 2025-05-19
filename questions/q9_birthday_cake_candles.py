def birthday_cake_candles(candles):
    candle_dict = {}

    # sort candles by their number and how many there are 
    for candle in candles:
        if candle in candle_dict:
            candle_dict[candle] += 1
        else:
            candle_dict[candle] = 1
    
    print(candle_dict)
    max_candle_count = 0

    # find out which candle number has the most occurrences in the candle_dict list
    for candle_value in candle_dict:
        candle_count = candle_dict[candle_value]

        if candle_count > max_candle_count:
            max_candle_count = candle_count
    
    return max_candle_count

candles_arr = [3, 2, 1, 3, 7, 7, 7, 7]
result = birthday_cake_candles(candles_arr)
print(result)