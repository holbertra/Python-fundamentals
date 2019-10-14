# total = 0
# total += 1
# # (value of total now) 1
# # -----

# total // 3
# #print(total)
# #print(total // 3)
# # 1
# # 0

# total += (2 // 3) + 3
# print(total)

# # 4
# # ------ 

# total + total
# # 4
# # 8
# print(total)
# print(total + total)

# num1 = 5.7
# num2 = 107.3
# (print( int( num2 // num1 )) )   # cast as int to get whole number

# banquet = False

# - Enter Event type: Banquet or Wedding,  and the number of attendees
# event_type = input("Enter Event type: Banquet or Wedding? ").lower()
# num_attendees = int(input("Enter number of attendees: "))

# if event_type == 'banquet':
# #    banquet = True
#     if num_attendees < 30:
#         print(num_attendees, "is Less than min number of attendees for your Banquet")
#     else:
#         print("Have a great banquet!")   
# elif event_type == 'wedding':
#  #   banquet = False
#     if num_attendees < 25:
#         print(num_attendees, "is Less than min number of attendees for your Wedding")
#     else:
#         print("Have a great wedding!")          
# else:
#     print(event_type, "is an Invalid Choice, Choose either Banquet or Wedding")  

#################################################
#################################################
# contracted_items = [
#    {
#       "id": "A001",
#       "name": "Daisy Paper Plates",
#       "price": 3.99
#    },
#    {
#       "id": "A002",
#       "name": "Solo Red Cups",
#       "price": 2.00
#    },
#    {
#       "id": "A199",
#       "name": "Dixie Paper Towels",
#       "price": 4.50
#    }
# ]
# purchased_items = [
#    {
#       "id": "A088",
#       "count": 32,
#       "price": 4.88
#    },
#    {
#       "id": "A002",
#       "count": 29,
#       "price": 3.40
#    },
#    {
#       "id": "A199",
#       "count": 2,
#       "price": 8.90
#    },
#    {
#       "id": "A332",
#       "count": 78,
#       "price": 22.78
#    },
#    {
#       "id": "A001",
#       "count": 10,
#       "price": 3.99
#    }
# ]

def calculate_savings(prev_price, current_price, amount, tax):
    """
    Function's purpose is to calculate and report savings on a purchase

    prev_price          (float number describing the price befores savings)
    current_price       (float number describing the price at purchasing)
    amount              (int number denoting how many were purchased)
    tax                 (float number describing the state's tax percentage)

    This function should return a float number describing how much was saved
    or a string stating "no savings occurred"
    """
    tax_percentage = tax / 100
    print("tax_percentage", tax_percentage)

    previous_total = (prev_price * amount) + tax_percentage
    current_total = (current_price * amount) + tax_percentage
    print("previous_total:", previous_total, "current_total", current_total)

    savings = previous_total - current_total
    print("savings", savings)
    
    # if savings > 0:
    #     return savings
    # else:
    #     return 'No savings occured'  

    return savings if savings > 0 else "no savings"

#print(calculate_savings(10.0, 7.00, 1, 7.0) )

#def calculate_savings(prev_price, current_price, amount, tax):

#for item in contracted_items:
# print(contracted_items[0])
# print(purchased_items[0])

# i = 0
# j = 0

# use unpacking to get price, count, etc.
# for i in range(len(contracted_items)):
#    for j in range(len(purchased_items)):
#       if i == j:
#          print(contracted_items[i]['id'], contracted_items[i]['price'],purchased_items[i]['price'],
#          purchased_items[i]['count'], "i:", i)


# to_filter = [
#    {
#       "name": "Anton",
#       "age" : 0
#    },
#    {
#       "name" : "Andy",
#       "age"  : 67
#    },
#    {
#       "name" : "Steve",
#       "age"  : 89
#    }
# ] 

# def filter_by_age(value):
#    return value["age"]  > 50

# greater_than_50 = list(filter( filter_by_age, to_filter ))  # cast as list, hint for one of challenges
# print(greater_than_50)

# def im_gonna_be_a_callback(x):
#    print(x)

# def i_take_callbacks(cb):
#    cb("Hello World")

# i_take_callbacks(im_gonna_be_a_callback)


# filtered_list = []   # alternative way
# for i in to_filter:
#    if i["age"] > 50:
#       filtered_list.append(i)

from datetime import datetime
import pprint

class Human:
   earthian = True

   def __init__(self, name, age, birthday):
      self.name = name
      self.age = age
      self.birthday = birthday

   def have_birthday(self):
      self.age += 1

   def greet(self):
      return f'Hello, my name is {self.name}'

   def human_globals(self):
      return globals()

mini_me = Human("Carson", 0, datetime(year=2019, month=6, day=27)) 

# pprint.pprint(mini_me.__dict__)      # - A dictionary representation of a class
# pprint.pprint(dir(mini_me))
#pprint.pprint(dir(""))
#help(mini_me)
#help(Human)

#pprint.pprint(globals())
# print(mini_me.greet())
# mini_me.have_birthday()
# print(mini_me.age)

# print(mini_me)
# print(id(mini_me))

numbers = [1,2,3,4,5]
def add_15(val):
   return val + 15

# adding = lambda x: x+15
# z = adding(15)
# print(z)

# my_numbers = set(map(lambda x:x+15, numbers))
# print(my_numbers)

class Cat:

   def __init__(self, name):
      self.name = name

   def __repr__(self):
      return f'<CAT: {self.name} >'

   # def __str__(self):
   #    return f'{self.name} is a cat.'

fido = Cat("Fido")

print(fido)
print(str(fido))
