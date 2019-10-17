
def binary_search(numbers, item, first=0, last=None):
    if not last:
        last = len(numbers) - 1

    if item == numbers[first]:
        return first
    elif item == numbers[last]:
        return last
    
    midpoint = (first + last) // 2

    if item == numbers[midpoint]:
        return midpoint

    elif item  > numbers[midpoint]:   # Right side
        return binary_search(numbers, item, midpoint + 1, last)

    elif item < numbers[midpoint]:  # Left side
        return binary_search(numbers, item, first + 1, midpoint - 1)

my_list = [1,2,3,4,5,6,7, 8, 9 ]
print(binary_search(my_list, 9))
