import random
replay='Y'

def caseOne(max):
  pcNum=random.randint(1,max)
  guess=int(input('Guess the computers number!\n'))
  
  while(guess!=pcNum):
    if(guess<pcNum):
      guess=int(input('Your number was too low! Guess again.\n'))
    else:
      guess=int(input('Your number was too high! Guess again\n'))
  global replay#have to use global to make it global
  replay=input(f'Congrats You Guessed {pcNum} Which Was The Right Answer!\nWould you like to play again\n[Y] Yes     [Any key] No\n').upper()
  replay=replay[0]

def caseTwo(max):
  notGuessed=True
  max=max+1
  min=0
  while(notGuessed):
    guess=int ((max-min)/2)+min
    try:
      acc=int(input(f'Is your number {guess}.\n [1] No its lower   [2] No its higher   [3] Yes\n'))
      if(acc==1):
        max=guess
      elif(acc==2):
        min=guess
      elif(acc==3):
        global replay#have to use global to make it global
        replay=input(f'The computer guessed {guess}!\nWould you like to play again\n[Y] Yes     [Any key] No\n').upper()
        replay=replay[0]
        notGuessed=False
      else: 
        pass
    except ValueError:
      print('You must enter a number!')
  
  
  
while(replay=="Y"):
  type=int(input("What mode would you like to play.\n[1] Guess Computer's Number [2]Computer Guesses Your Number\n"))
  if(type==1):
    try:#trys the value given by user
      max= int(input("Enter max number.\n"))
    except ValueError:#if theres a ValueError then itll set max to 100, error type can be seen in error msg
      max = 100
    caseOne(max)
  elif(type==2):
    x=True
    while(x):
      try:
        max=int(input('Enter a max number.(could be higher than the number you are thinking of)\n'))
        x=False
      except ValueError:
        print('You must enter a number!')
    caseTwo(max)
  else:
    pass
    




  

  
  