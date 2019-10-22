# states = {
#     'California' : 'CA',
#     'Texas' : 'TX',
#     'Kansas' : 'KS',
#     'Indiana' : 'IN'
# }

# cities = {
#     'CA' : 'Santa Barbara',
#     'TX' : 'Coppell',
#     'KS' : 'Lenexa',
#     'IN' : 'Carmel'
# }

# print(cities.get('CA'))

# for key, val in states.items():
#     print(key,val)

# print('############')    

# for state, city in cities.items():
#     print(state, city)   

# states['Ohio'] = 'OH'   

# print('############')

# for key, val in states.items():
#     print(key,val)

badge_dict = {
    1234: ["A2", "Z3"],
    2345: ["Z3", "H1"]
}

door = "V4"
badge_num = 1234

print(badge_dict.get(badge_num))   # ['A2', 'Z3']
badge_dict[badge_num].append(door)

message = """
This is the updated badge """
print(message)
print(badge_dict)


# badge_dict.update()
# product.update({"whatever": "the value"})
