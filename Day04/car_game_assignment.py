command= ''
is_checked = False
while True:
  command = input('> ').lower()
  if command == 'start':
    if(is_checked):
      print("Car already started ")
    else:
      print("Car started ")
      is_checked = True
  elif command == 'stop':
    if not is_checked:
     print('Car already stopped')
    else:
      print("Car Stopped ")
      is_checked = False
  elif command == 'help':
    print('''
    start - to start the car
    stop - to stop the car
    help - to know the instructions
    exit - to exit the game
    
    ''')
  elif command == 'exit':
    print("Game exit")
    break
  else:
    print( 
    '''
you have Entered Wrong input. Try Again.
press 'help' for info
    
    ''')
    continue
print("Thank You")