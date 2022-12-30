


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coin = {
    "penny": 0.01,
    "dime": 0.1,
    "nickle": 0.05,
    "quater": 0.25,
}

money=0

def report():
    """print available coffee resources and returns resources"""
    for items in resources:
        print(f"{items} : {resources[items]}")
    print(f"money: {money}")
        


def caffine_choice(choice):
    if choice in MENU:
        return MENU[choice]


def total_money(no_penny, no_dime, no_nickle, no_quater):
    p = coin["penny"]*no_penny
    d = coin["dime"]*no_dime
    n = coin["nickle"]*no_nickle
    q = coin["quater"]*no_quater
    return p+d+n+q

def compare(choice_details):
    for items in resources:
        if choice_details["ingredients"][items]>resources[items]:
            print(f"sorry there is not enough {items}")
            return False
    return True

def return_money(choice, total_money_collected):
    global money
    if MENU[choice]["cost"]>total_money_collected:
        print("Sorry that's not enough money.")
        return False
    else:
        print(f"Here is your ${round(total_money_collected-MENU[choice]['cost'],2)} in change")
        money=MENU[choice]['cost']
        print(f"Here is your {choice}☕ enjoy!!!")
        return True

while(1):
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=='report':
        report()
    elif choice=='off':
        exit()
    else:
        choice_details=caffine_choice(choice)
        if compare(choice_details)==True:
            print(f"{choice} cost={MENU[choice]['cost']}")
            print("please insert coins.")
            no_quater=int(input("How many quaters? : "))
            no_dime=int(input("How many dimes? : "))
            no_nickle=int(input("How many nickles? : "))
            no_penny=int(input("How many pennies? : "))
            transaction=return_money(choice,total_money(no_penny, no_dime, no_nickle, no_quater))
            if transaction==True:
                for items in resources:
                    resources[items]-=choice_details["ingredients"][items]
        