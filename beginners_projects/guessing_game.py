logo='''  ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗███╗   ██╗ ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔════╝     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗██║██╔██╗ ██║██║  ███╗    ██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██║██║╚██╗██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝╚██████╔╝███████╗███████║███████║██║██║ ╚████║╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                                                         
'''
import random
import os

def no_genrator():
    guessed_no=random.randint(1,100)
    return guessed_no

def level(choice_of_level):
    no_of_chances=5
    if choice_of_level=='easy':
        no_of_chances=10
    return no_of_chances


def game():
    print(logo)
    print("Welcome To The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty=level(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
    no=no_genrator()
    while(1):
        print(f"You have {difficulty} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if guess==no:
            print(f"You got it. The answer was {guess}.\n\n")
            play()
        elif guess<no:
            print("To low")
            difficulty-=1
        else:
            print("to high")
            difficulty-=1
        if difficulty==0:
            print("You run out of guesses. You lost!!! ")
            print(f"The anwer was {no}\n\n")
            play()

def play():
    while(1):
            print('''MENU:
1.play('p')
2.exit('e')''')
            choice3=input("Input your choice: ").lower()
            if choice3=='p':
                os.system('cls')
                game()
                
            elif choice3=='e':
                exit()
            else:
                print("You have entered wrong input, please enter right one.")
play()
