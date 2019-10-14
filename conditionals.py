# A conditional resolves to a boolean statement (True or False)
left = True
right = False

left != right #left & right are not equivalent
left == right # left and right are equivalent
left is right  # same identity
left is not right # not same identity

# Comparison Operators
age_1 = 23
age_2 = 45
age_1 > age_2
age_1 >= age_2
age_1 <= age_2

# Logical Operators
age_1 == 4 and age_2 < 22  # and operator
age_1 == 4 or age_2 < 22   # or operator  
not age_1 == 23

# Truth Tables
# a        b       a and b
#--------------------------
# True     True      True
# True     False     False
# False    True      False
# False    False     False
# 
# a         b       a or b
#--------------------------
# True      True      True
# True      False     True
# False     True      True
# False     False     False
#   

# x = 3
# name = 'Ryan'

# if x > 3 and name == 'Ryan':
#     if True:
#         print("I'm inside of an if if statement")
#     print("x is pretty big")
# elif x <= 3:
#     print('Maybe x is big, idunno')
# else:
#     print('Otherwise, no') 

# Challenge
# Take a name & age, and if person is under 18,
# say "NAME, you are not an adult",
# if the person is 21 and older 
#  

cool_name = False
name = input("Enter name: ")
age = int(input("age: "))

if name[0] == 'A' or name[0] == 'a':
    cool_name = True

if age < 18:
    print( "You are not an adult. ", name, "is a pretty Cool name though" if cool_name else " " ) 
#    print(f"{name}, is not an adult, you are only", age, end="")  # end="" suppresses carriage return
elif age >= 18 and age < 21:
    print( "You are not quite an adult.", name, "is a pretty Cool name though" if cool_name else " ")  
else:
    print( "You are a full adult. ", name, "is a pretty Cool name though" if cool_name else " ") 


# you = "Person"     
# you2 = you.replace('r', 'f')
# print(you2)

# if name[0].lower == 'a'

# Declare a number
# If the number is divisible by 3, print Fizz

# number = int(input("Enter number: "))

# if number % 3 == 0 and number % 5 == 0:  # alternate: if number % 15 == 0
#     print(number, "= FizzBuzz")
# elif number % 3 == 0:
#     print(number, "= Fizz")    
# elif number % 5 == 0:
#     print(number, "= Buzz") 
# else:
#     print(number, "is not divisible by either 3, 5 or 3 AND 5")       
