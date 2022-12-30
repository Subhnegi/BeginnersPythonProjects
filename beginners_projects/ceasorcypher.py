logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import os
def encrypt(message, shift):
    cypher_text=""
    for char in message:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift
            new_letter=alphabet[new_position]
            cypher_text+=new_letter
        else:
            cypher_text+=char
    print(f"The encoded message is : {cypher_text}")

def decrypt(cypher_text, shift):
    plain_text=""
    for char in cypher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position-shift
            new_letter=alphabet[new_position]
            plain_text+=new_letter
        else:
            plain_text+=char
    print(f"The decoded message is : {plain_text}")

while (1):
    print(logo)
    print('''
    ==========WELCOME==========
    Choose an option:
    1. encode('e')
    2. decode('d')
    3. exit('ex')''')

    choice = input("Enter your choice: ").lower()
    os.system('cls')
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    if choice=='e':
        encrypt(text,shift)
    elif choice=='d':
        decrypt(text,shift)
    elif choice=='ex':
        print("Good bye!!!!")
        exit()
    else:
        print("You have entered wrong input")