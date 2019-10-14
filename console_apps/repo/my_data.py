from datetime import datetime

class Vehicle:

    def __init__(self, make, model, year, vin, list_price):
        print("Vehicle::__init__(self, ...)")
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.list_price = list_price
        self.date_added = datetime.now()
        self.date_modified = datetime.now()

    def __repr__(self):
        return f'< CAR: { self.make }, { self.model }, { self.year }, { self.vin }, { self.list_price } >'

    def __str__(self):
        return f'< CAR: { self.make }, { self.model }, { self.year }, { self.vin }, { self.list_price } >'


class Inventory:

    def __init__(self, previous_inventory=[]):  # created only once
        print("Inventory::__init__(self, ...)")
        self.vehicles = previous_inventory
        self.date_created = datetime.now()
        self.date_modified = datetime.now()
    
    def __repr__(self):
        return f'< Inventory: { len(self.vehicles ) } cars >'
    
    def add_vehicle(self, make, model, year, vin, price):
        print("mydata::Inventory::add_vehicle()")
        new_vehicle = Vehicle(make, model, year, vin, price)
        self.vehicles.append(new_vehicle)
        self.date_modified = datetime.now()
        return 1

    def read_inventory(self):
        message = ""
        print("len:", len(self.vehicles))
        if len(self.vehicles):
             message += "ID  Make,  Model,  Year\n"
        for index, vehicle in enumerate(self.vehicles):
            message += f"{ index } - { vehicle.make }, { vehicle.model }, { vehicle.year }\n"
        return message
