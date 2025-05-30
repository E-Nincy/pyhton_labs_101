# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1, 10)
guess = None
attempts = 0
max_attempts = 3

while guess != num:
    guess = int(input("Guess a number betwen 1 and 10: "))
    
    if guess == num:
        print("Congratulations!! You won! .. nothing :P ")
        break
    else:
        attempts += 1
        print(f"Wrong guess. You have {max_attempts - attempts} tries left")
    
    if attempts == max_attempts:
        print("Sorry you have already used all your tries :( ")
        break