"""

Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the
change and the number of quarters, dimes, nickels, pennies needed for the change.

"""

cost, money = (float(input("Enter the cost of the item in dollars here: ")), float(input("Enter the money given here: ")))

while money < cost:
    print("You need to give more money than the cost")
    cost, money = (float(input("Enter the cost of the item in dollars here: ")), float(input("Enter the money given here: ")))

if money == cost:
    change = "No change"

else:
    leftover = money - cost
    leftover_cents = leftover * 100
    quarters = leftover_cents // 25
    leftover_cents = round(leftover_cents - quarters * 25, 0)
    dimes = leftover_cents // 10
    leftover_cents = round(leftover_cents - dimes * 10, 0)
    nickels = leftover_cents // 5
    leftover_cents = round(leftover_cents - nickels * 5, 0)
    pennies = leftover_cents

    change = {"Quarters": quarters, "Dimes": dimes, "Nickels": nickels, "Pennies": pennies}

print(change)

