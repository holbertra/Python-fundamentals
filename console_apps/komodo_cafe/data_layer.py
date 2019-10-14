
# NOTE! This uses 2 independent classes
class Item:
    """
    Item class is representation for menu items
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
         return f'[Item: { self.name}, ${ self.price } ]'

    def __str__(self):
         return f'[Item: { self.name}, ${ self.price } ]'     

    def change_price(self, new_price):
        """ to change price of the menu """
        self.price = new_price   
        return True 

    def change_name(self, new_name):
        """ to change name of menu item """
        self.name = str(new_name) 

class Menu:
    """
    A place to manage the menu 
    """

    def __init__(self, contents=[]):
        self.contents = contents

    def __repr__(self):
        return f'Menu: { self.contents }'

    def add_item(self, to_add):
        if isinstance(to_add, Item):         # Item is a Class
            self.contents.append(to_add)  
        else:
            to_add = False             
        return to_add   

    def read(self):
        return (self.contents)   

    def remove_item(self, to_remove):
        if to_remove in self.contents:
            index = self.contents.index(to_remove)
            self.contents.pop(index)
        else:
            to_remove = False
        return to_remove

# new_menu = Menu()
# new_item = Item("Apple", 9.99)
# new_item2 = Item("Banana", 5.00)
# new_item3 = Item("Avacado Toast", 25.00)
# new_item4 = Item("Opus One", 100.00)

# new_menu.add_item(new_item)
# new_menu.add_item(new_item2)
# new_menu.add_item(new_item3)
# new_menu.add_item(new_item4)


# print(new_menu.read())