import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bid_dict={}
bid_count=True

def auctionbid():
    x=-1
    y=""
    for name in bid_dict:
        if int(bid_dict[name])>x:
            x=int(bid_dict[name])
            y=name
    print(f"Congratulation!!!!  {name} for winning the bid with amount ${bid}")
while(1):
    os.system('cls')
    print(logo)
    name=input("What is your name? :  ")
    bid=input("What is your bid? : $")
    bid_dict[name]=bid
    x=input("Are there any other bidders: type 'yes' or 'no'. : ").lower()
    if x=='no':
        auctionbid()
        break
    elif(x!='yes'):
        bid_count=False
    
    
        
    