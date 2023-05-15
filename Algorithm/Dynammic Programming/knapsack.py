def DP_knapsack(profit, weight, length, size):

    k = [[0]*(size+1) for _ in range(length+1)]

    for i in range(length+1):
        for j in range(size+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif weight[i-1] <= j:
                k[i][j] = max(k[i-1][j], profit[i-1]+k[i-1][j-weight[i-1]])
            else:
                k[i][j] = k[i-1][j]
    return k


def traceback(profit, weight, length, size):
    k = DP_knapsack(profit, weight, length, size)

    i = length
    j = size
    while i > 0 and j > 0:
        if k[i][j] == k[i-1][j]:
            i -= 1
        else:
            print(
                f'Item {i} with profit {profit[i-1]} and weight {weight[i-1]}')
            j -= weight[i-1]
            i -= 1


# driver code
size = int(input('Enter the size of your Knapsack: '))

# length = int(input('Enter the length of your Items: '))
# profit = [(input('Items: ').split() for x in range(length))]
profit = [int(profit) for profit in input('Profit: ').split()]
weight = [int(weight) for weight in input('Weight: ').split()]

coin = DP_knapsack(profit, weight, len(profit), size)
print(f'Maximum Profit is: {coin[len(profit)][size]}')
traceback(profit, weight, len(profit), size)
