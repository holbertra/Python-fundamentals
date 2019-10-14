
#Collections
#List
#CRUD create, read, update and delete.

# https://www.w3schools.com/python/python_lists.asp

my_list = [2,4,3]            #create
str_list = ["bananas", "apples", "pears"]
first_item = my_list[0]      #Read
my_slice = my_list[::-1]  # - reverse list [3, 4, 2]
#my_slice = list(my_list.reverse)
#print(my_slice)

my_list.append(["hello, world"]) 
#my_list[3][1] 
my_list[1] = 6          # - update
my_list.insert(1,8)     # - insert
print(my_list)
testing = my_list.pop()  # capture what is deleted 
#print(testing)  
my_list.extend(["hello", "world"]) 
my_list.remove("hello")  # remove first value found
my_list.clear()          # update clears the list
str_list.reverse()       # https://www.w3schools.com/python/ref_list_reverse.asp
print(str_list)

multi_list = [2,4,3, "string"]            
new_list = multi_list.append(55)
print(new_list)   # this prints None !Beware of this because the return value is None

# But this works
multi_list.append(55)
new_list = multi_list 

# For Loops

x = 0
for i in range(10):   # Shared scope with the file
    x = 1 + i
    if i >= 7:
        print("i:", i, "about to break")
        break
    if i > 8:
        print("continue")
        continue

    a = i + i
print(x, a, i)

# While Loops
# n = 8
# while n >= 0:
#     print("not yet")
#     n -= 1
# print("finally done")

# Dictionary
# Key-Value pairing, unordered & mutable
# my_dictionary = {
#     "name" : "Rich Holbert",
#     "age"  :  "55 feel like 25"
# }

# print(my_dictionary["name"])
# print(my_dictionary.get("name"))
# my_dictionary["name"] = "riCh hOLBer#t"
# my_dictionary["hobby"] = "guitars"
# print(my_dictionary["hobby"])
# print(my_dictionary["age"])

# NOTE the difference
for item in my_dictionary.items():
    print(item)    # prints: ('name', 'Rich Holbert'), ('age', '55 feel like 25'), ('hobby', 'guitars')             
for item in my_dictionary:
    print(item)   # prints: name, age hobby 

# print(my_dictionary.keys())   # dict_keys(['name', 'age', 'hobby'])
# print(my_dictionary.values()) # dict_values(['Rich Holbert', '55 feel like 25', 'guitars'])
# print(my_dictionary.items())  # dict_items([('name', 'Rich Holbert'), ('age', '55 feel like 25'), ('hobby', 'guitars')])

# Functions
# def func_name(parameters)
# arguments are passed - parameters are received
# scope

# v = ""
# def change(x):
#     v = "velocity"
#     return x + 1

# print(change(12))
# print(v)  # the v outside of loop 

# Classes  
# https://www.w3schools.com/python/python_classes.asp
# Custom data type object that contains methods & attributes

class Animal:

    def __init__(self, kingdom):
        self.kingdom = kingdom

    def get_kingdom(self):
        return self.kingdom


class Human(Animal):

    def __init__(self, kingdom, name, age):
        super().__init__(kingdom)
        self.name = name 
        self.age = age

    def speak(self):
        return f'Hello, I am {self.name}'

me = Human("Camlot", "Sir Adam", 25)
print(me.get_kingdom())

# Virtual environment
# isolated environ in python used to test and share projects in to order
# keep dependencied local
# will use the version of python you are currently using
