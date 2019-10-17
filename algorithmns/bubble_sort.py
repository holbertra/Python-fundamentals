# Visualization of sortss
# https://visualgo.net/en/sorting
# https://www.youtube.com/watch?v=kPRA0W1kECg  "15 sorting algos in 6 minutes"

def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

numbers = [44, 7, 12]
(bubble_sort(numbers))
print(numbers)

