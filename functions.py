# What is a function?

def function_name_here(x):
    # Code Block
    print(x)
    return "some data"

print(function_name_here("Python is cool"))  
something = function_name_here("I'm data")
print(something)

# multiple parameters


def cash_register(total, tendered):
    """" This takes two numbers and compare them """

    answer = ""

    if tendered < total:
        answer = "Hey, more money pal!"
    elif tendered == total:
        answer = "Have a nice day" 
    else:
        answer = "I owe you money"  

    return answer

# answer = cash_register(67, 30)
# print(cash_register)
# help(help)

# Default return statement

def combine(x,y,z):
    """
    Takes 3 number and prints their sum
    """
    return (x+y+z)

what_is_this = combine(1,2,3)    
print(what_is_this)

if combine(12,12,12):
    print("found none here")

    

# None define


