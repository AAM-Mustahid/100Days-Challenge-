#assignment operator
#bitwise OR Operator
a = 5; #in binary 101
b = 3; # in binary 11
x= a|b; #after adding them 111 comes. so it is equal to 7
print(x)
#bitwise XOR Operator(if two bit is same then it will give zero in bit)
y = 5 #101
z = 3 #011
c = y^z #110
print(c) # 110 == 6

#identity Operator
z = 10
t = 50
print(z is t)
print (z  is not t)

#Membrship OPrator
b = ["Mustahid","Abbu","Zakir"]
print("ustahid" in b)
print("ustahid" not in b)