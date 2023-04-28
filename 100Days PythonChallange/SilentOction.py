from turtle import clear
from art import logo_auction

print(logo_auction)
# oxtion_people=[]
member_details={}
def who_won(bid_members):
    highest_bid=0
    winner=""
    for i in bid_members:
        bidding_amt=bid_members[i]
        if bidding_amt>highest_bid:
            highest_bid=bidding_amt
            winner = i
    print(f" the bid is won by {winner} with a max price of {highest_bid} ")
print("WELCome to The Secret Auction program \n ")
auction_again=True
while(auction_again):
    key=input("Enter your name : ")
    value=int(input("Enter the auction amount $"))
    member_details[key]=value
    print(member_details)
    
    # oxtion_people.append(member_details)
    any_other_persion_for_auction=input("Is there any other person who want's to partecipate for auction type yes / no ? ")
    if(any_other_persion_for_auction=="no"):
        auction_again=False
    # elif any_other_persion_for_auction=="yes":
        # clear()
who_won(member_details)