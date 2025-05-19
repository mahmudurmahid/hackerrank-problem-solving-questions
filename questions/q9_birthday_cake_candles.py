def birthday_cake_candles(candles):
    candle_counter = {}

    # sort candles by their number and how many there are 
    for candle in candles:
        if candle in candle_counter:
            candle_counter[candle] += 1
        else:
            candle_counter[candle] = 1
    
    print(candle_counter)
    max_candle_counter = 0

    # find out which candle number has the most occurrences
    for candle_num in candle_counter:
        counter = candle_counter[candle_num]

        if counter > max_candle_counter:
            max_candle_counter = counter
    
    return max_candle_counter

candles_arr = [3, 2, 1, 3, 7, 7, 7, 7]
result = birthday_cake_candles(candles_arr)
print(result)