my_numbers = [1, 2, 3, 4, 5]


def sum_recurs(numbers, count):
    print(f'calling sum_recurs {count} times')
    count += 1
    if len(numbers) == 1:
        return numbers[0]
    else:
        print(f'from else: returning {numbers[0]} + {numbers[1:]}')
        return numbers[0] + sum_recurs(numbers[1:], count)

my_count = 1
sum_recurs(my_numbers, my_count)

