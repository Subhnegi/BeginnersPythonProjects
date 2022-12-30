
import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_card=[]

dealers_card=[]

def dealer_score(deal_card,game_start):
    if game_start==True:
        first_card=random.choice(cards)
        second_card=random.choice(cards)
        dealers_card.append(first_card)
        dealers_card.append(second_card)
    if deal_card==True:
        another_card=random.choice(cards)
        dealers_card.append(another_card)

def player_score(deal_card,game_start):
    if game_start==True:
        first_card=random.choice(cards)
        second_card=random.choice(cards)
        players_card.append(first_card)
        players_card.append(second_card)
    if deal_card==True:
        another_card=random.choice(cards)
        players_card.append(another_card)
    

def game():
    print(logo)
    want_another=True
    
    players_card.clear()
    dealers_card.clear()
    game_start=True
    deal_card=False
    player_score(deal_card,game_start)
    dealer_score(deal_card,game_start)
    print(f"Your cards = {players_card} , your score = {sum(players_card)}")
    print(f"Computer's first card = {dealers_card[0]}")
    while(want_another== True):
        choice2=input("Type 'y' to get another card and 'n' to pass: ").lower()
        if choice2=='y':
            game_start=False
            deal_card=True
            player_score(deal_card,game_start)
            if 11 in players_card and sum(players_card)>20:
                players_card.remove(11)
                players_card.append(1)
            print(f"Your cards = {players_card} , your score = {sum(players_card)}")
            if sum(players_card)>21:
                print("Your score went over 21. YOU LOSE!!!")
                play()
        else:
            want_another=False
    if sum(dealers_card)<17:
        game_start=False
        deal_card=True
        dealer_score(deal_card,game_start)
    print(f"Your final hand = {players_card} , your final score = {sum(players_card)}")
    print(f"compuer's final hand = {dealers_card} , computer's final score = {sum(dealers_card)}")
    if sum(dealers_card)>21:
        print("Computer's score went over 21. YOU WIN!!!")
    elif sum(players_card)>sum(dealers_card) or sum(players_card)==21:
        print("YOU WIN!!!")
        play()
    elif sum(players_card)==sum(dealers_card):
        print("It's a DRAw!!!")
        play()
    else:
        print("YOU LOSE!!!")
        play()
def play():
    while(1):
        print('''======WELCOME======
                    MENU:
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
