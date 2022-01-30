import random

elements = [1, 2, 3]
num_of_rounds = 10
num_of_wins = 0
num_of_loss = 0

def idk():
  while(True):
    try:
      users_choice = (input('The number of rounds is set to 10.\nDo you want to change it?[Y/n]\n'))
      usl = users_choice.lower()
      if usl == 'y':
        round_choice = int(input('How many rounds do you want to play?\n(NOTE: Number of rounds cannot be more than 15!)\n'))
        if round_choice > 15:
          print("You have entered a number over 15")
          break
        elif round_choice == 0:
          break
        else:
          global num_of_rounds
          num_of_rounds = round_choice
          break
      elif usl == "n":
        break
      else:
        print('Invalid input!')
    except:
      print('Invalid input!')
      
def c_choice():
  if computer == 1:
    print("Computer chose Rock")
  elif computer == 2:
    print("Conputer chose Paper")
  else:
    print("Computer chose Scissor")
    
def u_choice():
  if user == 1:
    print("You chose Rock")
  elif user == 2:
    print("You chose Paper")
  elif user == 3:
    print("You chose Scissor")
  else:
    print('Invalid input!')
  

idk()

while(True):
  
  try:
    computer = random.choice(elements)
    user = int(input('\n1 is for Rock\n2 is for Paper\n3 is for Scissor\nWhat is your choice?\nEnter your choice: '))

    if user == computer:
      print('Its a draw')
    elif user+1==computer or user == 3 and computer == 1:
      num_of_loss += 1
      print("You lose this round")
    elif user-1==computer or user == 1 and computer == 3:
      print('You win this round!')
      num_of_wins += 1
    else:
      print("Invalid input!")
      continue
  except:
    print('Invalid input!')
    continue
  
  u_choice()
  c_choice()

  num_of_rounds -= 1
  print(f"You only have {num_of_rounds} rounds left")
  just_for_fun = input('Press enter to continue')
    
  if num_of_rounds == 0:
    if num_of_wins>num_of_loss:
      print('You win!')
    elif num_of_loss>num_of_wins:
      print('You lose!')
    else:
      print('Its a draw!')
    wanna_continue = input('\nDo you want to play another match?[Y/n]')
    if wanna_continue == 'n':
      break
    elif wanna_continue == 'y':
      idk()
    else:
      break
  else:
    pass
