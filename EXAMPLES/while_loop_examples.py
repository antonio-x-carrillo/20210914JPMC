#!/usr/bin/env python

print("Welcome to ticket sales\n")

while True:  # <1>
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("Please enter number of tickets")
        continue  # <2>
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # <3>

    quantity = int(raw_quantity)  # could validate via try/except
    if quantity > 16:
        print("Max number of tickets is 16")
        continue
    print("sending {} ticket(s)".format(quantity))
