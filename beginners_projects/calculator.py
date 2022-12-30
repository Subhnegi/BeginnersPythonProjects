logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


operations = {"+": add,
              "-": sub,
              "*": mul,
              "/": div}


def calculator():
    '''This function is for airthmatic problems'''
    print(logo)
    want_continue = True
    num1 = float(input("Enter your first number: "))

    while want_continue == True:

        for symbols in operations:
            print(symbols)

        operation = input("pick a operation symbol for above: ")
        num2 = float(input("Enter your second number: "))
        function = operations[operation]
        answer = function(num1, num2)
        print(f"{num1}{operation}{num2}= {answer}")
        cont = input(
            "Do you want to perform more operations?type 'yes' or 'no': ").lower()
        if cont == 'no':
            want_continue = False
            calculator()
        elif cont == 'yes':
            num1 = answer
        else:
            print("You have entered wrong input\n")
            if input("type 'e' to exit or 'c' to continue: ").lower()=='e':
                exit()
            else:
                want_continue = False
                calculator()
calculator()
