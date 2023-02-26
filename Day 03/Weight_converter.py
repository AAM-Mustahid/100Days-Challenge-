input1 = input("Choose which data you want to input here. press 'k' Kg and 'p' Pound:\n" )
if('k'in input1 ): 
  print("You have selected Kg to Pound \n")
  input2=float(input('Enter Your Weight In KG: \n'))
  pound = input2*2.20462
  print(f'Your {int(input2)} is equal to {pound:.2f}')
elif('p' in input1) :
  input2 = float(input('Enter your weight in Pound: \n'))
  kg = input2*0.453592
  print(f'{int(input2)} is equal to {kg:.2f}')
else:
  print("You have entered wrong Keyword. Please try again later\n")

print("Thank you.")
  