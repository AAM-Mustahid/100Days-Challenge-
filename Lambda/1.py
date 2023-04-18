#Write a Python program to create a lambda function
# that adds 15 to a given number passed in as an argument,
#also create a lambda function that multiplies argument x with argument y and
#prints the result

x = lambda a: a+15
z = lambda x,y: x*y
print(x(10))
print(z(20,10))
