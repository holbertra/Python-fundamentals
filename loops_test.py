import datetime

puzzle = open('frequencies.txt', 'r').read().split("\n")
number = [int(i) for i in puzzle ]

########################
# For loop
########################
total = 0
print( "Start for:", datetime.datetime.now().time() )
for x in number:
    total += x

print("End for:", datetime.datetime.now().time(), "total:", total, "\n#") 

##### Reset the vars ######
total = 0  
x = 0      

########################
# While loop
########################
print("Start while:", datetime.datetime.now().time())
while x < len(number):
    total += number[x]
    x += 1

print("End while:", datetime.datetime.now().time(), "total:", total)     

# Start for: 00:00:50.714608
# End for: 00:00:50.714608 total: 497
#
# Start while: 00:00:50.714608
# End while: 00:00:50.728977 total: 497

# 728977 - 714608 = 14,369

