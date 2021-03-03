import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper =  '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)  

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

player = input('What is your play? (Rock, Paper or Scissor)? \n').lower()

computer = random.randint(1,3)
if computer == 1:
    computer = 'rock'
elif computer == 2:
    computer = 'paper'
elif computer == 3:
    computer = 'scissor'

if player == computer:
    print('Nobody won! Try again...')
elif player == 'rock' and computer == 'paper':
    print(f'Player: {rock}')
    print(f'Computer: {paper}')
    print('Computer wins!')
elif (player == 'rock' and computer == 'scissor'):
    print(f'Player: {rock}')
    print(f'Computer: {scissor}')
    print('Player wins!')
elif (player == 'scissor' and computer == 'rock'):
    print(f'Player: {scissor}')
    print(f'Computer: {rock}')
    print('Computer won!')
elif (player == 'scissor' and computer == 'paper'):
    print(f'Player: {scissor}')
    print(f'Computer: {paper}')
    print('Player won!')
elif player == 'paper' and computer == 'scissor':
    print(f'Player: {paper}')
    print(f'Computer: {scissor}')
    print('Computer won the game!')
