def knap(arr,w):
    arr.sort(key=lambda x: x[0]/x[1], reverse=True)
    tot_value = 0.0

    for profit,weight in arr:
        if(weight<=w):
            w = w-weight
            tot_value = tot_value + profit
        else:
            # knapsack is full
            tot_value = tot_value + (profit * (w/weight))
            break
    return tot_value


arr = [(60, 10), (100, 20), (120, 30)]
w = 50
print(knap(arr,w))