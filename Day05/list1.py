list = [10,20,30,40,50]
print(list)                    
#Newlist = list((10,30,40))
#print(Newlist)

#accessing list

print(list[1])
print(list[-1])
print(list[2:4])
print(list[-4:])
print(list.index(30)) #check wheather the 30 in list or not
if 40 in list: #check wheather the 30 in list or not
  print(True)

#change value
print(list)
list[:2]=[1000,2000,3000]
print(list)
list[0:2] = [100]
print(list)
'''
if i insert more than range remaining value will inserted orderly in list. But if we are insert less than range then remaining item will cut down. 
'''

# i can insert at the last of the list 
list.append(2)
print(list)

#insert specified index 
list.insert(4,1)
print(list)

# we can add another list , tuple , dictionary in a list

new_list =["mustahid","Jahid","Asif","Zabir"]
print(list.extend(new_list)) # extend does not resturn any value. thats why it shows none

print(list) # now it shows extending values because extend methos already extended our previous list.  


#Removing Elements from my list

list.remove("Asif")
print(list)
list.pop(0) #for specified index
list.pop() #remove last index of list
print(list)
del list[0] #also delete 
list2=list.copy();
print(list2)

#if we use del then it can delete the list. 

# del list2
#print(list2) # we can not print it because list 2 delete from memory
#list.clear() # it removes all elements from list
#print (list)


#loop through list by indexing number

for number in range(len(list)):
  print(list[number]) 
i = 0
while i < len(list):
  print(list[i])
  i+=1
#list compression
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

