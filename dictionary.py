# Dictionaries
# dict

my_dictionary = {
    "key" : "value",
    "key2" : 78
}

product = {
    "id"         :  2345872425,
    "description": "A yellow submarone",
    "price"      :  9.99,
    "weight"     :  9001,
    "depart"     : "grocery",
    "aisle"      :  3,
    "shelf"      :  "B"
}

#print(product["price"])
location = (product["aisle"], product["shelf"])
#print(location)
#print(product.get("quanity"))   # use .get when unknown or unsure it exists

product["aisle"] = 4
product["department"] = "guy's grocery games"

# for key in product:
#     print(product[key])

# A list of the values   
# print(product.values()) 
# print(product.keys()) 
# product["whatever"] = "the value"
product.update({"whatever": "the value"})

# Challenge
you = {}
data = [ ("name", "Rich") , ("age", 55), ("class", "Python") ]

for x in data:
    you.update({ x[0]: x[1] })
print(you)    

for k, v, in data:
   you[k] = v    

you.update(data)   # 1 line solution
print(you)

print(f'Your age is { you["age"]}')





