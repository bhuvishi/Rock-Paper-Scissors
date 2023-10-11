rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

#Write your code below this line 👇
user_choice = int(
    input(
        'Welcome to the Rock Paper Scissors Simulator.\nYou can choose from the following:\nEnter 0 for rock\nEnter 1 for paper\nEnter 2 for scissors\n'
    ))

computer_choice = random.randint(0, 2)

if user_choice == 0:
    print(rock)

elif user_choice == 1:
  print(paper)

elif user_choice ==2:
  print(scissors)

if computer_choice == 0:
    print(rock)

elif computer_choice == 1:
  print(paper)

elif computer_choice ==2:
  print(scissors)

if computer_choice == user_choice:
  print("It's a draw.")

if computer_choice == 0 and user_choice ==1:
  print('You won!!')

elif computer_choice == 0 and user_choice ==2:
  print('You lost!!')

if computer_choice == 0 and user_choice ==1:
  print('You won!!')

if computer_choice == 0 and user_choice ==2:
  print('You lost!!')

if computer_choice == 0 and user_choice ==1:
  print('You won!!')

if computer_choice == 0 and user_choice ==2:
  print('You lost!!')
