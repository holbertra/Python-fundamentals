from my_data import Vehicle, Inventory

current_inventory = Inventory()

def retrieve_inventory_list():
    retrieved = current_inventory.read_inventory()   # Call Inventory::read_inventory() 
    return retrieved if retrieved else "No vehicles in inventory"

def add_vehicle(make, model, year, vin, price):  #this add_vehicle() calls the Inventory class add_vehicle()
    print("my_repo::add_vehicle()")   
    return "Added Vehicle" if current_inventory.add_vehicle(make, model, year, vin, price) else "Error"