# https://pythonspot.com/recursion/
# https://stackabuse.com/understanding-recursive-functions-with-python/

my_items = [1, 2, 3, 6, 89]

def recursive_sum(numbers):
    print("start:len(numbers):", len(numbers))
    if len(numbers) == 1:   # A one item list
        print("if branch: return", numbers[0])
        return numbers[0]
    else:
        print("else branch: return", numbers[0], " + ", numbers[1:])
        return numbers[0] + recursive_sum(numbers[1:]) #numbers list gets shorter for each recursive call

print("recusive sum:", recursive_sum(my_items))
print("using sum():", sum(my_items))

""" Output:
[1, 2, 3, 6, 89] len: 5
start: 5
else branch: return 1  +  [2, 3, 6, 89]
else branch: return 2  +  [3, 6, 89]
start: 3
start:len(numbers): 4
else branch: return 2  +  [3, 6, 89]
start:len(numbers): 3
else branch: return 3  +  [6, 89]
start:len(numbers): 2
else branch: return 6  +  [89]
start:len(numbers): 1
if branch: return 89
recusive sum: 101
using sum(): 101
"""

"""
def recursive_sum(numbers):
    if len(numbers) == 1:   # A one item list
        return numbers[0]
    else:
        return numbers[0] + recursive_sum(numbers[1:]) #numbers list gets shorter for each recursive call
                            if (len(numbers)) == 1:
                                    return numbers[0]
                                    
"""                                    

# Fibonacci sequence
# 0,1,1,2,3,5,8,13,. . . 
# starts with 0 & 1
# subsequent numbers are the sum of the previous two

# def fib(numbers, current=1, previous=0, count=0):    # first iteration: current = 1 prev = 0
#     if count < numbers:
#         return fib(numbers, current+previous, current, count+1)
#     else:
#         return current

# print(fib(8))  # = 34
# print(fib(300)) 

# alternate version
# def fib(cycles, current=1, previous=0):
#     if cycles:
#         return fib(cycles-1, current+previous, current)
#     else:
#         return current

# print(fib(8))

"""
* | * | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  - cycle
0 | 1 | 1 | 2 | 3 | 5 | 8 | 13| 21| 34|  - Fib num
"""

