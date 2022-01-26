import random

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

#Write your code below this line 👇
user_choice = int(input("Type 0 for rock, 1 for paper, and 2 for scissors: "))

if user_choice == 0:
  print("You chose rock")
  print(rock)
elif user_choice == 1:
  print("You chose paper")
  print(paper)
elif user_choice == 2:
  print("You chose scissors")
  print(scissors)
else:
  print("Invalid choice. Please try again.")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
  print("The computer chose rock")
  print(rock)
elif computer_choice == 1:
  print("The computer chose paper")
  print(paper)
elif computer_choice == 2:
  print("The computer chose scissors")
  print(scissors)
else:
  print("Invalid choice. Please try again.")

if user_choice == 0 and computer_choice == 0:
  print("It's a tie!") 
elif user_choice == 0 and computer_choice == 1:
  print("You won!")
elif user_choice == 0 and computer_choice == 2:
  print("You lost!")
elif user_choice == 1 and computer_choice == 0:
  print("You won")
elif user_choice == 1 and computer_choice == 1:
  print("It's a tie!")
elif user_choice == 1 and computer_choice == 1:
  print("It's a tie!")
elif user_choice == 1 and computer_choice == 2:
  print("You lost!")
elif user_choice == 2 and computer_choice == 0:
  print("You lost!")
elif user_choice == 2 and computer_choice == 1:
  print("You win!")
elif user_choice == 2 and computer_choice == 2:
  print("It's a tie!")