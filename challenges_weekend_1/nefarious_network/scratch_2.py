employees = open('employees.csv', 'r').read().split("\n")   # readlines() bring it in as List object
access_list = open('employees.csv', 'r').read().split("\n")

employees.pop(0)
employees.pop()
access_list.pop(0)
access_list.pop()

#- get rid of duplicate ip addresses from the access list
ip_list = []
for ip in access_list:
    if  ip[0] not in ip_list:
        ip_list.append(ip[0])