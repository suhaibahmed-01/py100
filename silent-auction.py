from replit import clear
from art import logo
print(logo)


bid_records = {}
bidding_finished = True


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = "" 
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

  
while bidding_finished:
  name = input("\n\nWhat is your name? : ")
  bid = int(input("\n\nWhat is your bid?: $"))
  bid_records[name] = bid
  should_continue = input("Are there any more bidders remaining?\nType 'yes to continue, else type 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bid_records)
  elif should_continue == "yes":
    clear()
  
