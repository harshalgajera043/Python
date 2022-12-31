from replit import clear
from art import logo
# print(logo)

bid_dict = {}
def bidder(Name, bid_amount):
    bid_dict[Name] = bid_amount

any_more_bidder = True
while any_more_bidder == True:
    print(logo)
    Name_bidder = input("What is your name?\n")
    Bid = int(input("What is your bid?\n"))
    bidder(Name = Name_bidder, bid_amount = Bid) #use of predefine bidder function which use user name and bid amount as a inputs
    bidder_remain = input("Any other bidder are their type 'yes' or 'no'?\n")
    if bidder_remain == "no".lower():
        any_more_bidder = False
    clear()

max_bid = 0
lst_user = []
lst_bid = []
for key in bid_dict:
    lst_user.append(key) #make a list of bidder
    lst_bid.append(bid_dict[key]) #make a list of bids
    if max_bid <= bid_dict[key]:
        max_bid = bid_dict[key]
    index_max_bid = lst_bid.index(max_bid) #index value of maximum bid amount
    winner = lst_user[index_max_bid] #use of index value of max bid to know the bid winner.
print(logo)
print(f"{winner} make the highest bid of {max_bid}")