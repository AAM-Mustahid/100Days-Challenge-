def required_coins(n,coins):
    ways = [0]*(n+1)
    ways[0] = 1

    for coin in coins: 
        for j in range (len(ways)):
            if coin <= j:
                ways[j]+=ways[j-coin]
    
    return ways[n]



#driver code
coins = [1,3,5]
change = int(input('How many amount you want to Change: '))
print('Your available coin: ',coins)
total_ways=required_coins(change,coins)
print(f'Total Number of ways to Change: {total_ways}')