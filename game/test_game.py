
MAX_DIGITS = 3
MAX_GUESS = 5

# print(f'Please enter a {MAX_DIGITS} digit number')
# print(f'I have thought of a {MAX_DIGITS} digit number. Can you guess it?')

# print("I\'m sorry Dave, I lied")

# while MAX_GUESS > 0:
#     MAX_GUESS -= 1
#     print(f'You have {MAX_GUESS} attempts left, Dave')

# positions = ["_", "_", "_"]
# guess = ["1", "2", "3"]
# positions[1] = guess[1]
# print(positions)

#calculate lower and upper range
i = 0
lower_range, upper_range = "", ""
while i < MAX_DIGITS:
    lower_range += "0"
    upper_range += "9"
    i += 1
range = f'{lower_range}' + ' - ' + f'{upper_range}'

print(range )
