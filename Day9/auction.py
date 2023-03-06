from art import logo
print(logo)
bid_person = {}
n = 0
highest = 0
winner =""

def find_high_bid(bid_person):
        highest = 0
        winner =""
        for bidder in bid_person:
            bid_amount = bid_person[bidder]
            if(highest < bid_amount):
                highest = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest}")

        

while(n == 0):


    name = input("enter the name\n")
    bid_price = int(input("Enter the bid price\n"))
    bid_person [name] = bid_price
    b = (input("is there anyone who want to bid \t YES \t NO\n"))

    if(b == "NO"):
        n = 1
        find_high_bid(bid_person)


