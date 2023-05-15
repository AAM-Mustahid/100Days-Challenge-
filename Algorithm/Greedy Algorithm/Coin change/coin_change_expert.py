#problem solved of coin change
import time
start = time.time()
def min_coin(coins,payout):
    count = 0 
    min_coin = 0
    coins.sort(reverse=True)
    for i in coins:
        if payout>0:
            min_coin = int(payout/i)
            count += min_coin
            payout-= min_coin*i
    
    print(count)









#driver code
size = int(input())
coin = list(map(int,input().split()))
payout = int(input())
min_coin(coin,payout)

print('process time: %s seconds'%(time.time()-start))