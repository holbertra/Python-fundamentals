access_list = [ 
    ["ip_address", "access_date"], 
    [ "69.45.135.45", "6/6/2019"],
    [ "69.45.135.45", "5/4/2019"],
    ["204.73.38.135", "8/1/2019"]

]

#print(access_list)

employee_list = [
    ["id", "first_name", "last_name", "email", "ip_address"],
    ["1", "Ameline", "MacEvilly", "amacevilly0@irs.gov", "204.73.38.135"],
    ["2", "Ede", "Fallow", "efallow1@bloomberg.com", "95.202.195.133"],
    ["3", "Sephira", "Konerding", "skonerding2@apple.com", "193.55.226.107"]
]

#- get rid of duplicate ip addresses from the access list
ip_list = []
for ip in access_list:
    if  ip[0] not in ip_list:
        ip_list.append(ip[0])

ip_list.remove("ip_address")

# - strip out just the ip colummn from the employee list
emply_ip_list = []
for ip in employee_list:
    if ip[4] not in emply_ip_list:
        emply_ip_list.append(ip[4])

emply_ip_list.remove("ip_address")

# print("access:", ip_list)
# print("employ:", emply_ip_list)

# ip_list =  ['56', '44', '22', '99', '107']
# emply_ip_list = ['24', '44', '56', '67', '86', '87']

#- list the ip addresses from the access list that DO NOT appear in the employee list
hacker_ip = []

for x in ip_list:
    if x not in emply_ip_list:   # Finally got this to work, DON'T use 2 variables & only 1 for loop
        hacker_ip.append(x)

print("hacker_ip", hacker_ip)

   
