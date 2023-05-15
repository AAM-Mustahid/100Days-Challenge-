# measure my compile time for this code
import time
start_time = time.time()




def min_coin (coin):
    coins = [1,2,5,10,20,50,100,200,500,2000]
    min_coin=0
    count = 0
    changeCOIN=[]
    coins.sort(reverse=True)
    
    for i in coins:
        if coin>0:
            while i<=coin :
                changeCOIN.append(i)
                min_coin = int(coin/i)
                count+=min_coin
                coin-=min_coin*i
    if coin <0:
        print('Change is not possible')
    else: 

        print(f'Minimum coins: {count}')
        print('change coin is: ')
        for j in changeCOIN:
            print(j,end=' ')
    
    print('process time: %s seconds'%(time.time()-start_time))







#driver code
coin = int(input('Enter the amount you want to exchange: '))
min_coin(coin)