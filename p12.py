import os
import sys

def loadInventory():
    try:
        f = open("inventory.txt", 'r')
        machine = {}
        for line in f:
            line = line.strip()
            data = line.split(" ")
            machine[data[0]] = [float(data[1]), int(data[2])]

        return machine
    except IOError:
        print "File inventory.txt does not exist."
        sys.exit()
    except TypeError:
        print "Type error"
    """
    with open("inventory.txt", 'r') as f:
        machine = {}
        for line in f:
            line = line.strip()
            data = line.split(" ")
            machine[data[0]] = [float(data[1]), int(data[2])]

        return machine
    """
def displayItems(machine):
    """
    the function will display all the items, their price, and the amount
    """
    for key in machine:
        print key, machine[key][0], machine[key][1]

def chooseItemAndPay(machine):
    item = raw_input("Choose an item that you like: ")
    if item in machine:
        print item, machine[item][0], machine[item][1]
        """
        show the item, cost, and amount that customer choose
        """

        if machine[item][1] <= 0:
            print item, "Sold Out!"
            print
            return 0
        """
        if the amount of item that customer choose is less than 1, then it is sold out!
        """

        itemValue = float(machine[item][0])
        remaining = itemValue
        while remaining > 0:
            """
            show the customer how much money they need to pay left
            """
            print remaining, "dollars left"
            opt = int(raw_input("press 1 for cash, press 2 for coins, press 3 for cancel): "))
            if not opt in [1, 2, 3]:
                print "Input again!"
                continue

            if opt == 1:
                """
                if customer wants to pay with cash
                """
                money = float(raw_input("Please insert cash (dollar): "))
                remaining -= money
            if opt == 2:
                money = float(raw_input("Please insert coins (cents): "))
                remaining -= money/100
                """
                if customer wants to pay with coins, so it mush be divided by 100
                """
            if opt == 3:
                """
                if the customer wants to cancel, the machine will refund the money that the customer gave
                """
                print "Refund:", itemValue-remaining, "dollars"
                print
                return 0

        machine[item] = [machine[item][0], machine[item][1]-1]
        #print "Take", item, "and the change", (0.0-remaining), "dollars"
        print "Take %s and the change %.2f dollars" %(item, 0.0-remaining)
    else:
        print "Choose again!"

    print
    return itemValue

def main():
    machine = loadInventory()
    income = 0

    while True:
        """
        shows the customers how much the machine gain in total after the customer bought his or her item
        """
        displayItems(machine)
        income += chooseItemAndPay(machine)
        print "The machine gains", income, "dollars!"

if __name__ == '__main__':
    main()
