puzzle = open('frequencies.txt', 'r').read().split("\n")
number = [int(i) for i in puzzle ]

# Challenge
#Find final frequencys
#For loop
#While loop
#Python built-in (see google)

freq = 0
for x in number:
    freq += x            # for summing, left operand must be different from right operand
print("freq:", freq)

freq = 0
x = 0
print("len:", len(number))

while x < len(number):
    freq += number[x]    # for summing, left operand must be different from right operand
    x += 1
print("freq:", freq)

freq = 0
freq = sum(number)       # Built-in
print("freq:", freq)

