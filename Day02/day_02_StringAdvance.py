#formatting
a = int (input('Enter Your First Number: \n'))
b = int (input('Enter your second number: '))
divide =" {:.2f} ".format (a/b)
result = a/b
print(divide)
print('%.2f' %result)
print(round(result,2))

a = 'mustahid'
b = 'is '
c = 'going to be a leader'
result = "{0} {1} {2}".format(a,b,c)
print(result)

