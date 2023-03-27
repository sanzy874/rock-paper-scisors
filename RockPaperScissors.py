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


choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if choice==0:
  print(rock)
elif choice==1:
  print(paper)
elif choice==2:
  print(scissors)
           
comp_choice=random.randint(0,2)
if comp_choice==0:
  print("Computer chose:",rock)
elif comp_choice==1:
  print("Computer chose:",paper)
elif comp_choice==2:
  print("Computer chose:",scissors)

#outputs
if choice==0 and comp_choice==2:
  print("You win!")
elif choice==2 and comp_choice==0:
  print("You lose!")
elif choice==1 and comp_choice==0:
  print("You win!")
elif choice==1 and comp_choice==2:
  print("You lose!")
elif choice==0 and comp_choice==1:
  print("You lose!")
elif choice==2 and comp_choice==1:
  print("You win!")
elif choice==comp_choice:
  print("It's a tie!")
