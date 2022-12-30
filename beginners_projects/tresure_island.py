print("=======WELCOME TO TRESURE ISLAND=======")
print("Your mission is to find the tresure.")
choice=input('''You're at a cross road. Where you want to go? "left" or "right" \n''')

if choice.lower()=="left":
    choice=input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim: to swim across.\n ''')
    if choice.lower()=="wait":
        choice=input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n''')
        if choice.lower()=="yellow":
            print("You have found the treasure.\n YOU ARE RICH")
        else:
            print("You have eaten by monsters. You are DEAD")

    else:
        print("You have eaten by monsters. You are DEAD")
else:
    print("You have fallen into a volcano. You are DEAD")