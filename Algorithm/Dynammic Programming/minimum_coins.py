import sys


def Dp_min_coins(coins, length, total):
    t = [sys.maxsize for x in range(total+1)]
    t[0] = 0
    c = [-1] * (total+1)
    for i in range(length):
        for j in range(coins[i], total+1):
            t[j] = min(t[j], 1+t[j-coins[i]])
            c[j] = i

    return t[total], c


def traceback(coins, c, total):
    coin = []
    while total != 0:
        coin.append(coins[c[total]])
        total -= coins[c[total]]
    return coin


# driver code
Coins = [7, 2, 3, 6]
total = int(input('Enter the amount You want to change: '))
result = Dp_min_coins(Coins, len(Coins), total)
print(f'Minimum Number Required for the change {total} is {result[0]}')
print('The coins are: ', traceback(Coins, result[1], total))
