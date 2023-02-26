#understanding With a guessing game
secret_Number = 9
guessing_count = 1
Guessing_Limit = 3

while guessing_count<= Guessing_Limit:
  Guessing_Number = int( input("Your Number: "))
  if(Guessing_Number==3):
    print("You can not guess number 3,Try again ") #To understanding the continue keyword
    continue
  if(Guessing_Number==secret_Number):
    print("you have won ")
    break
  guessing_count+=1
else:
  print("You failed, Try again later ")
print("Thank You")
  