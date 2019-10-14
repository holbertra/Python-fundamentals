

import manager

while True:
    prompt = """
    What would like to do?
    ----------------------
    1) View menu
    2) Add item to menu
    3) Change item
    4) Remove
    5) Quit
    > """
    option = int(input(prompt))

    if option == 5:
        quit()
    elif option == 1:
 #       print(current_menu.read())
        print(manager.read_menu())
    
    elif option == 2:
        new_name = input("What is the item's name? >")
        price = float(input("What is the item's price >"))
        print(manager.create_item(new_name, price))
    
    elif option == 3:   #- 3) Change item
        for i, item in enumerate(manager.current.meu.contents):
             print(f"{ i }> {item}")
        which_item = int(input("Which item would like to edit? >"))
        new_name = input(f"Change name (Leave blank to not edit) >")
        new_price = input("Change price (default is {to_edit.price}) >")

        print(manager.change_item(which_item, new_name, new_name))

    elif option == 4:          #- 4) Remove Item
        print("HIT OPTION 4")
    
    else:
        pass   # continue on in loop


    # print(option)