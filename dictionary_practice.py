states = {
    'California' : 'CA',
    'Texas' : 'TX',
    'Kansas' : 'KS',
    'Indiana' : 'IN'
}

cities = {
    'CA' : 'Santa Barbara',
    'TX' : 'Coppell',
    'KS' : 'Lenexa',
    'IN' : 'Carmel'
}



for key, val in states.items():
    print(key,val)

print('############')    

for state, city in cities.items():
    print(state, city)   

states['Ohio'] = 'OH'   

print('############')

for key, val in states.items():
    print(key,val)

