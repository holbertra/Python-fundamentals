import komo_manager

while True:
    prompt = """
    What would like to do?
    ----------------------
    1) Add a new badge
    2) Edit a badge
    3) List all Badges
    4) Delete a Badge
    5) Quit
    > """
    option = int(input(prompt))

    if option == 5:
        print("Goodbye!")
        quit()

    elif option == 1:  #Add a New Badge
        print("Option 1: Adding a new badge. . . ")
        badge_num = int(input("Enter badge number >"))
        access_doors = []
        access_doors.append(input("Enter door to access >"))
        response = input("Would you like to add another door (y/n?) >")
        while response == 'y':
            access_doors.append(input("Enter door number >"))
            response = input("Would you like to add another door (y/n?) >")

#        print("komo_ui:access_doors:", access_doors)
        print(komo_manager.add_badge(badge_num, access_doors))
        input("Press Enter to continue...")


    elif option == 2: # Edit a badge
        print(komo_manager.list_badges())
        badge_num = int(input("Enter badge number to edit >"))
        badge = komo_manager.get_badge(badge_num)
#        print("komo_ui:option2:badge:", badge)

        # Adding or removing access doors of selected badge
        prompt = """
        What would like to do?
        ----------------------
        1) Add a door
        2) Delete a door
        3) Quit
        > """
        option = int(input(prompt))
        print("komo_ui:option2:option", option )
        if option == 3:
            quit()

        elif option == 1:  # Add a door(s)
            door = print("Enter door number to add >")

        elif option == 2:
        else:
            pass
    
    elif option == 3: 
        print("--- All current active badges ---")
        print(komo_manager.list_badges())
    
    elif option == 4:  # Delete a Badge
        badge_num = int(input("Enter badge number to delete >"))
        print(komo_manager.delete_badge(badge_num))
        input("Press Enter to continue...")                         
    else:
        pass   # continue on in loop        