# # Fill out the truth table
# a       b       not (a and b or b)
# ----------------------------------
# False   False    True
# True    False    True
# False   True     False  
# True    True     False
# ========================================

# Each student that has an A in their name, print their age.
# Make your program able to handle any list of students (this format below)
# **** can be done in 1 line

students = [("AJ", 25), ("XD", 19), ("JA", 27), ("IS", 27)]

for x in students:
    name, age = x  # unpacking
    if 'A' in name:
      print(name, age)

####### Alternate Solution ########
for a, b in students:
    if 'a' in a.lower():
        print(a, 'is', b, 'yrs old')   

for a, b in students:               
    print(a, 'is', b, 'yrs old') if 'a' in a.lower()
 