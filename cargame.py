started = False
while True:
  command = input('Enter your command: ')    #put the above code on continue loop, and also add the logic for wrong input, and breaking condition
  if command.lower() == 'start':
    if started:
      print('Car is already started')
    else:
      print('Car started')
      started = True

  elif command.lower() == 'stop':
    if not started:
      print('Car is already stopped')
    else:
      print('Car stopped')
      started = False

  elif command.lower() == 'help':
    print('''start - to start the car
stop - to stop the car''')
  elif command.lower() == 'quit':
    print('thanks for playing the game')
    break
  else:
    print('Sorry, I dont understand your command')