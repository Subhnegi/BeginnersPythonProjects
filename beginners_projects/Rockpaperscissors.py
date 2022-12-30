

import random
randomno = random.randint(1, 3)


def game(comp, player):
    if (comp == player):
        print("its a tie")
    elif (comp == 'r'):
        if (player == 'p'):
            print("paper covers rock you win!!!")
        elif (player == 's'):
            print("rock crushes scissors you loose!!!")
    elif (comp == 'p'):
        if (player == 'r'):
            print("paper covers rock you loose!!!")
        elif (player == 's'):
            print("scissor cuts paper you win!!!")
    elif (comp == 's'):
        if (player == 'r'):
            print("rock crushes scissors you win!!!")
        elif (player == 'p'):
            print("scissor cuts paper you loose!!!")


def display(n):
    rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    if n == 'r':
        print(rock)
    elif n == 'p':
        print(paper)
    elif n == 's':
        print(scissors)


while (1):
    print('''
    ==========WELCOME==========
    Choose an option:
    1. Play('p')
    2. exit('e')''')
    choice = input("Enter your choice: ").lower()

    if choice == 'p':
        print("Lets play ROCK PAPER SCISSORS!!!!!")
        player = input("Enter your choice Rock(r) Paper(p) Scissors(s): \n")
        if (player.lower() == 'r' or player.lower() == 'p' or player.lower() == 's'):
            display(player.lower())
            if (randomno == 1):
                comp = 'r'

            elif (randomno == 2):
                comp = 'p'

            elif (randomno == 3):
                comp = 's'

            print("comp choice :\n")
            display(comp)
            game(comp, player.lower())
        else:
            print("You have entered wrong choice. Please enter right choice.")
    elif choice == 'e':
        exit()
    else:
        print("You have entered wrong choice. Please enter right choice.")
