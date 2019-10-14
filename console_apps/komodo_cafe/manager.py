from data_layer import Item, Menu

current_menu = Menu()

def read_menu():
    return current_menu.read()

def create_item(name, price):
    new_item = Item(name, price)
    current_menu.add_item(new_item)
    return f"{new_item } was successfully added"

def change_item(index, name, price):
    to_edit = current_menu.contents[index]
    price = float(price or to_edit.price)
    name = name or to_edit.name

    if name:
       to_edit.change_name(name)
    if price:
        to_edit.change_price(price)
    return f"{to_edit } was successfully modified"