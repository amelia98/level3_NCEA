def get_reserve(reserve):
    print("Auction Manager")
    print("Reserve must be greater than or equal to $0.00")
    reserve = (read_int("What is the auction reserve?"))

def get_bids(names, bids):
    print("\nAuction has started")
    name=""
    while name.upper() !='F':
        print("Highest bid is ${:.2f}".format(float(max(bids))))
        name = input("What is your name (\"F\" to finish)")
        if name.upper() !='F':
            names.append(name)
            bid=(read_int("What is you bid?"))
            if bid <= max(bids):
                print("You will need to make a higher bid.")
            bids.append(bid)

def show_bids(names, bids):
    print("\nBidding History")
    for i in range (1,len(names)):
        print("{} bid ${:.2f}".format(names[i], bids[i]))

def show_report(bids):
    if len(names) == 1:
        print("No bids, Auction did not meet reserve price.")
    if max(bids) >= reserve:
        print("Auction won by " + names[bids.index(max(bids))] + " with a bid of ${:.2f}".format(float(max(bids))))
    else:
        print("Auction did not meet reserve price")

def read_int(prompt):
    choice = -1;
    while choice < 0:
        try:
            choice = float(input(prompt))
        except ValueError:
            print("Not a valid integer")
    return choice

#main routine
names = [0,]
bids = [0.00,]
reserve = 0

get_reserve(reserve)
get_bids(names, bids)
show_report(bids)
show_bids(names, bids)
