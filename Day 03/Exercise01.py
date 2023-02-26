name = input('Enter Your name: \n')
length = len(name)
if(length<3):
  print("Name must be atleast 3 charecter")
elif(length>50):
  print("Yes,Bro thats cool")
else:
  print("Names looks good")