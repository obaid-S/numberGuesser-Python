import random
replay='Y'
def start(max):
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
  

while(replay=="Y"):
  try:#trys the value given by user
    max= int(input("Enter max number.\n"))
  except ValueError:#if theres a ValueError then itll set max to 100, error type can be seen in error msg
    max = 100
  start(max)
  
  