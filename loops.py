# Loops
# for loops

# animals = ["Jaguar", "Raccoon", "Fox", "Cat", "Toucan"]

# for animal in animals:
#     print(animal)

# for (i=0; i<len(animals); i++)  C# example  

# for i in range(1,101):

# for i in range(10):    # - Matches 10 times 
#     for j in range(10): 
#         if i == j:  
#             print("They match", i, j)   

# expenses = [
#     ("McDonalds", 12.00),
#     ("Steam", 49.99),
#     ("Rent", 900.00)
# ] 

# total = 0.0

# for expense in expenses:
#    
#     print("itemized:", total)

# print("total:", total)   

# While Loop
# x = 0
# while x < 100:
#     print(x)
#     x += 4

products = ["nvidia", "amd", "arm", "intel", "risc"]
search_term = "amd"
# Create a while loop that searches this list until
# it finds the search term

# x = 0
# while x < len(products) and search_term not in products[x]:
#     print("x:", products[x])
#     x += 1
# else:
#     print("Found search_term") 

if search_term in products:
    print(products.index(search_term), search_term) 
else:
    print("not found")         





