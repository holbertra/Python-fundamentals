#To create a virtual environment: <python> -m venv <a-name-here>
#To activate virtual env:
#   Windows <a-name-here>/Scripts/activate
#   Mac(linux): source <a-name-here>/bin/activate
# To verify: Terminal shoud have virt-env on the left
# PIP PIP Installs Packages
#

import requests
from pprint import pprint

# response = requests.get("https://rickandmortyapi.com/api/character/3")

# data = response.json()
# print(type(data))
# #pprint(data.items())

# for key, value in data.items():
#     print(key, value, '\n')
#     if key == 'episode':
#         print(key, value, '\n')

api_url = "https://rickandmortyapi.com/api/"
char_response = requests.get(api_url + "character")  # get response object

#print(char_response.reason)

try:
    data = char_response.json()  # data defined here is accessed by print(data) below - outside try block
except Exception:
    data = None  

print(len(data['results']))   # - 20
#print(data['results'][-1])  # - top level keys
choices = data['info']['count']  # - 493 number of characters

choice = input(f"Pick a number between 1 and {choices} > ")

chosen = requests.get(api_url + "character/" + choice)
print(chosen.headers)
chosen_one = chosen.json()
print(chosen_one['name'])

"""
Some notes:
    HTTP -> GET, POST, PUT, DEL

"""



        