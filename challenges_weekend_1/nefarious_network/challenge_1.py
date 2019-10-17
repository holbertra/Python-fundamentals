#####################################
# - Challenge 1    Answer: 105 unauthorized ip addresses # 
# - See enumerate() for this
# - See puzzle.py for nested for loops - a One-to-Many mapping of the two files
# -
# - Helps:
# - https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
# - https://realpython.com/python-csv/
#####################################
import csv

# - Read in the csv files
# with open('employees.csv') as csvDataFile:
#     employ = list(csv.reader(csvDataFile))
# with open('access_list.csv') as csvDataFile:
#      access = list(csv.reader(csvDataFile))

# access_list = [ 
#     ["ip_address", "access_date"], 
#     [ "69.45.135.45", "6/6/2019"],
#     [ "69.45.135.45", "5/4/2019"],
#     ["204.73.38.135", "8/1/2019"]

# ]
# #print(access_list)

# employee_list = [
#     ["id", "first_name", "last_name", "email", "ip_address"],
#     ["1", "Ameline", "MacEvilly", "amacevilly0@irs.gov", "204.73.38.135"],
#     ["2", "Ede", "Fallow", "efallow1@bloomberg.com", "95.202.195.133"],
#     ["3", "Sephira", "Konerding", "skonerding2@apple.com", "193.55.226.107"]
# ]

# # - get rid of duplicate ip addresses from the access list
# ip_list = []
# for ip in access_list:
#     if  ip[0] not in ip_list:
#         ip_list.append(ip[0])

#- list the ip addresses from the access list that DO NOT appear in the employee list
hacker_ip = []

for x in ip_list:
    if x not in emply_ip_list:     # Finally it works! My problem I was using two variables, ONLY NEEDED ONE
        hacker_ip.append(x)
        print("x:", x)

print("hacker_ip", hacker_ip)   

#######################################
#  Alternate Solution per Adam
#######################################
employees = open('employees.csv', 'r').read().split("\n")   # readlines() bring it in as List object
print(employees)
access_list = open('employees.csv', 'r').read().split("\n")
print(access_list)

employees.pop(0)
employees.pop()
access_list.pop(0)
access_list.pop()


modified_employees = []
for row in employees:
    info = row.split(",")
    modified_employees.append(info[4])

modified_access_list = []
for row in access_list:
    info = row.split(",")
    modified_access_list.append(info[0])

unauthorized = [ ip for ip in modified_access_list if ip not in modified_employees]

#unauthorized = []
# for ip in modified_access_list:
#     if ip not in modified_employees:
#         unauthorized.append(ip)


#######################################
# Solution form Adam 
#######################################

# employees = open('employees.csv', 'r').readlines()   # readlines() bring it in as List object
# print(employees)
# access_list = open('employees.csv', 'r').readlines()
# print(access_list)

# # - Func to convert any csv file
# def convert_to_list_of_dict(the_list):      # - generic func that applies to any number columned file (both csv files)
#     keys = the_list.pop(0).split(',')       # - take off the column header - resolved left to right
#     to_return[]
#     for row in the_list:
#         entry = {}
#         values = row.split(",")
#         for i, key in enumerate(keys):
#             entry[key] = values[i]
#         to_return.append(entry)
    
#     return the_list

# accesses = convert_to_list_of_dict(access_list)
# users = convert_to_list_of_dict(known_users)

# bad_events = []
# for event in accesses:
#     bad = True
#     for user in users:
#         if event["ip_address"] == user["ip_address"]
#             bad = False
#         if bad:
#             bad_events.append(event)   

# print(len(bad_events))











          

     








     






    





  






# file_open = open('employees.csv', 'r').read().split("\n")
# employ_list = (i for i in file_open)    # - I want to read this in as a tuple

# file_open = open('access_list.csv', 'r').read().split("\n")
# access_list = [i for i in file_open]

# x = 1
# while x < 5:
#     print(employ_list[x])
#     x += 1

# y = 1
# while y < 5:
#     print(access_list[y])
#     y += 1    