# my_items = [1, 2, 3, 6, 89]

# def recursive_sum(numbers):
#     if len(numbers) == 1:
#         return numbers[0]
#     else:
#         return numbers[0] + recursive_sum(numbers[1:])

# print(recursive_sum(my_items))
# print(sum(my_items))

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
def fib(cycles, current=1, previous=0):
    if cycles:
        return fib(cycles-1, current+previous, current)
    else:
        return current

print(fib(8))

"""
* | * | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  - cycle
0 | 1 | 1 | 2 | 3 | 5 | 8 | 13| 21| 34|  - Fib num
"""

