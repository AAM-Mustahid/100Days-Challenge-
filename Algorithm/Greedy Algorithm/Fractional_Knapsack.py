def fractional_knapsack(weight, value, capacity):
    ratio = [v/w for w, v in zip(weight, value)]
    index = list(range(len(value)))
    index.sort(key=lambda i: ratio[i], reverse=True)
    used_items = []
    max_value = 0

    for i in index:
        if weight[i] <= capacity:
            used_items.append((value[i], weight[i]))
            max_value += value[i]
            capacity -= weight[i]
        else:
            used_items.append((value[i], weight[i]))
            max_value += value[i]*capacity/weight[i]
            break
    return max_value, used_items


# driver code
weight = list(map(int, input('Weight: ').split(' ')))
value = list(map(int, input('Value: ').split(' ')))
capacity = int(input('Enter the capacity of Your Knapsack: '))

max_value, used_items = fractional_knapsack(weight, value, capacity)
#print(f'Maximum value of the Knapsack can hold: {max_value: .3f}')
print('%.4f' % max_value)
print(f'items_used(value:weight): {used_items}')
