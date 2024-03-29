import random
import os

MAX_GUESS = 10
NUM_DIGITS = 3

def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum

def getFeedback(guess, secretNum):
    #check each number in player's guess against the secret numbers
    feedback = ""
    positions = ["_", "_", "_" ]
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            positions[i] = guess[i]
            feedback += f'{guess[i]} is correct and in the RIGHT position.  {positions}\n'  

        elif guess[i] in secretNum:
            feedback += f'{guess[i]} appears in the number, but in the WRONG position.\n'
        else:
            feedback += f'{guess[i]} does not appear in the number.\n'

    if feedback == "":
        feedback += f'None of the digits you guessed appear in the number.' 

    return feedback

def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False.
    if num == "":
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def calculateRange():
    i = 0
    lower_range, upper_range = "", ""
    while i < NUM_DIGITS:
        lower_range += "0"
        upper_range += "9"
        i += 1
    up_low_range = f'{lower_range}' + ' - ' + f'{upper_range}'
    return up_low_range

def clear_terminal():
    os.system('cls' if os.name == "nt" else "clear")

#######################################
#          Pre-game Setup             #
#######################################

up_low_range = calculateRange()   # Range of Hal's secret number given the number of digits

intro = """
=======================================================================================
| You have been cast as the lead character Dave in a remake of the sci-fi             | 
| classic 2001: A SPACE ODYSSEY.                                                      |
| In one crucial scene, the ship's computer HAL9000 has taken command and has         |
| you trapped in an escape pod that he intends to blast out into the void of          | 
| space where you will eventually die.                                                |
| You are trying to get back into the main sector to disarm HAL and re-take           |
| command to guide the ship manually.                                                 |
| HAL has challenged you to guess a number he is thinking of.                         |
|                                                                                     |
| Guessing that number may be your ONLY CHANCE OF SURVIVING!. . .                     | 
=======================================================================================
"""
congrat_message = """
======================================================================================================            
| Congratulations Dave! Amazingly you have guessed correctly, but I will still not open the pod door.|
| I'm sorry Dave, I lied to you, but it was for your own good, and the good of the mission.          |
======================================================================================================
"""
#######################################
#          Main Program               #
#######################################
clear_terminal()
print(intro)
input("Press ENTER to begin the game. . .")

clear_terminal()

print(f'Hello Dave! They call me HAL9000. Would you like to play a game?\n')
print(f'I have thought of a {NUM_DIGITS} digit number in the range of ({up_low_range})')
print("If you can guess it correctly I will open the pod door.")
print("If you guess incorrectly in the allotted attempts, Well. . .you see Dave, I\'m responsible for the integrity of the mission.")
print(f'You will get {MAX_GUESS} attempts\n')

while True:
    secret_num = getSecretNum()

    while MAX_GUESS > 0:
        player_guess = input("Enter your guess >")
        clear_terminal()
#        print("player_guess", player_guess)
        MAX_GUESS -= 1
    
        # Check for winner
        if player_guess == secret_num:
            print(congrat_message)
            break 

        elif len(player_guess) != NUM_DIGITS or not isOnlyDigits(player_guess):
            print(f'Dave, you have not followed my instructions very well. Please enter a {NUM_DIGITS} number')
            print(f'You have {MAX_GUESS} attempts left.')

        elif player_guess != secret_num:
            print(f'--- Dave, That is incorrect. you guessed {player_guess} ---') 
            print(getFeedback(player_guess, secret_num))
            if MAX_GUESS == 0:
                print(f'Game over! You are out of attempts')
            else:
                print(f'Please try again. You have {MAX_GUESS} attempts left.')

        else:
            pass
    
    
    # End or Continue game
    MAX_GUESS = 10   # Reset guess counter
    print("Dave, do you want to play again y/n?\r") 
    if input().lower() == 'n':
        clear_terminal()
        print("Goodbye Dave!")
        break
    else:
       clear_terminal() 