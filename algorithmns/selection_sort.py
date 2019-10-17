def selection_sort(numbers):
    for i in range(len(numbers)):
        lowest_value_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[lowest_value_index]:
                lowest_value_index = j
        numbers[i], numbers[lowest_value_index] = numbers[lowest_value_index], numbers[i]

my_list = [34, 55, 190, 2, 0, 57]
selection_sort(my_list)
print(my_list)
