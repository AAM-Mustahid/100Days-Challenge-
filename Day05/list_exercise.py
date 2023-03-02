a = input('enter list numbers: ')
#b = a.split(",")
#print(b)
x = [int(x) for x in a.split(" ")]
max = 0
#for finding max number
for i in  x:
  if i>max:
    max = i
  

print(max)