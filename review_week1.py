# variables - don't use reserved words

clear = "Yes" 

name, age = "Adam", 25   # tuple without parens ()  
print(type(name))

def multple_returns(a,b):
    data = 0
    if a > b:
        data = b, a
    return True, data

print(multple_returns(2,1)) 
success, corrdinate = multple_returns(2,1) 

something = {}  # empty dictionary
something.update({"random": 56})  # update method, or
something["cool"] = 51          # direct assignment
print(something)

#######
# Functions
#######

# def func(x):
#     first, second = x
#     return f'{x,y}'

# n = 3, "y"
# captured = func(3, 5)
# print(captured)
# print(34 == "34")

#######
# Loops
#######

items = [1,2,3,4,5]
for item in items:
    k = item + 12

print(k)    # k exists outside of for loop

z = True
flag = 0

while z:
    flag += 1
    scope = "Do I exist"
    if flag > 34:
        z = False

print(scope) 
scope = ""       

if scope:
    potato = "Spuds"
else:
    potato = ""    

print(potato)    




 

