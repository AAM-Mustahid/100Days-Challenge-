def DP_knapsack(profit, weight, length, size):
    k = [[0]*(size+1) for _ in range(length+1)]
    for i in range(length+1):
        for j in range(size+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif weight[i-1] <= j:
                k[i][j] = max(k[i-1][j], profit[i-1] + k[i-1][j-weight[i-1]])
            else:
                k[i][j] = k[i-1][j]
    return k[length][size]

# driver code
size = int(input('Enter the size of your Knapsack: '))
length = int(input('Enter the length of your Items: '))
profit = [int(profit) for profit in input('Profit: ').split()]
weight = [int(weight) for weight in input('Weight: ').split()]

print(DP_knapsack(profit, weight, length, size))