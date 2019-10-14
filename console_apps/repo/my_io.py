import os
import time

import my_repo as manager

prompt = """
Welcome to the Sleasy Car Saleseman portal!
What would you like to do?

1) View inventory
2) Add vehicle to inventory
3) Change vehicle information
4) Exit

>"""

def clear_terminal():
    os.system('cls' if os.name == "nt" else "clear")

while True:
#    clear_terminal()
    choice = input(prompt)

    if choice == "1":  # View inventory
        # clear_terminal()
        print(manager.retrieve_inventory_list())     # call my_repo::retrieve_inventory_list()
        input("Press enter to go back to main screen")
        pass

    elif choice == "2":   # Add vehicle to inventory
#        clear_terminal()
        print("Adding vehicle to inventory...")
        make = input("Enter vehicle make > ")
        model = input("Enter vehicle model > ")
        year = input("Enter vehicle year > ")
        vin = input("Enter vehicle vin > ")
        price = input("Enter vehicle listing price > ")
        print("Adding vehicle to inventory...")
        print(manager.add_vehicle(make, model, year, vin, price))  #- mydata.py::Inventory::add_vehicle(make,....)


    elif choice == "4":
        clear_terminal()
        print("")
        print("Exiting")
        clear_terminal()
        exit()

