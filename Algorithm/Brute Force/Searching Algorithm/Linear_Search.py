def linear_search(list,Search_Value):
    for i in list:
        if i== Search_Value:
            print(f'{Search_Value} is Found')
            break
    else:
        print(f'{Search_Value} is Not Found')    
         
        
        


    


#driver code
list = list(map(int,input('Input: ').split(" ")))
Search_Value = int(input('search Values: '))

#result = linear_search(list,Search_Value)
linear_search(list,Search_Value)
