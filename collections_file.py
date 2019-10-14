#Lists - can be of ANY type

names = ["Adam", "Justin", "Xzavier"]
students = [
    "The Rock",
    "Charles",
    "The Undertaker",
    "Big Show",
    "Tony Stark",
    6,
    4 + 1j,
    [
        "nested lists",
        "are cool",
        [
            56
        ]
    ]
]

# names[0] = "Potato"
# names.append("Thanos")   #add to END of list
# print(names[-1])
# print(type(students[-1][-1]))

# names.insert(1, "Debbie")
# print(names)
# students.extend(names)
# print(students)
# names.pop(0)   # remove from index
# print(names)
# print(len(students))
# # print(len(names))

# students.remove("Tony Stark")  # - find 1st instance of & remove, based on type
# print(students)

#                  [start:stop at, but not include :step by n]
# new_list = students[0:3:1]  # alt [:3:1]
# print("new_list: \n", new_list, "\n")
# reverse_list = students[::-1]
# print("reverse_list: \n", reverse_list, "\n")
# reversed_again = list(reversed(students))
# print("reversed_again: \n", reversed_again)

# x = [
#     12,
#     34
# ]
# y = ["yes", "again"]
# print(x + y)

# Tuples - similar to lists but immutable
my_tuple = (12, 32)
my_name = ("Rich", "Holbert")
f_name, l_name = my_name   # unpacking tuple into two variables
print(f_name, l_name)

tuple_names = ("Matthew", "Mark", "Luke", "John", "Judas")
something = tuple_names[2:3]
# print(something)
# print(tuple_names[5]) - Index out of range error 

# tester = ("John",)
# print(type(tester))

# Sets - No duplicate items
#
# states = { "Indiana", "Alaska", "Texas" }
# # print(type(states))
# states.add(90)
# states.remove("Alaska")    # Remove item, error if not there
# states.discard("Canada")   # Removes item if there, silently
# print("states:", states)
# print(states.clear())

# print("Indiana" in states)

# Single item set don't need comma, like a tuple does
# Sets are mutable

# my_test = {"single item"}
# print(type(my_test))

# sentence = "Mary had a little Lamb"
# list_of_words = sentence.split()
# print(list_of_words)
# list(sentence)

my_names = ["Wallaby", "Bakersfield", "colGAte", "COcaCOla"]
print("my_names - before:", my_names )
# remove colgate
# add Crest
# Change cocacola to lowercase
# grab every other item in the list
# Print each name individually

my_names.remove("colGAte")
my_names.append("Crest")
my_names[2] = my_names[2].lower()  # - Must reassign!

print("my_names - after:", my_names)

print(my_names[0:3:2]) 

for x in my_names:
    print(x)

print("\n".join(my_names))    # Alternate way 

   



      

