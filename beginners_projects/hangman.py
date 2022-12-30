import os


import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


words = ''''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()
while(1):
    print(logo)
    print('''
        ==========WELCOME==========
        Choose an option:
        1. Play('p')
        2. exit('e')''')
    choice = input("Enter your choice: ").lower()

    if choice == 'p':
        print("Lets play HANGMAN!!!!!")
        chosen_word = random.choice(words)
        lives=6
        str=""
        # print(f"{chosen_word}")
        blanks = []
        for i in range(0, len(chosen_word)):
            blanks.append("_")
        print(str.join(blanks))
        while ("_" in blanks):
            guess_letter = input("guess a letter: ").lower()
            os.system('cls')
            if guess_letter in blanks:
                print("You have already guessed this letter")
                print(f"No. of lives left = {lives}")
            for i in range(0, len(chosen_word)):
                letter = chosen_word[i]
                if letter == guess_letter:
                    blanks[i] = letter
            print(str.join(blanks))
            if guess_letter not in chosen_word:
                lives-=1
                print(stages[lives])
                print("You have guessed wrong, you loose 1 life!!!")
                print(f"No. of lives left = {lives}")
                print(str.join(blanks))
            if lives==0:
                print("you lose!!!!")
                print(f"The right answer was {chosen_word}")
                break
        if lives>0:
            print("you win!!!")
    elif choice == 'e':
        exit()
    else:
        print("You have entered wrong choice. Please enter right choice.")
