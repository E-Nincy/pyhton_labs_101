# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it


import string

word_to_guess = "universe"
max_attempts = 8
guessed_letters = set()
correct_letters = set()
word_display = ["_"] * len(word_to_guess)


print("Welcome to Hangman, and may the odds be ever in your favor :) Let's beggin!")
print(f"You have {max_attempts} attempts to guess the word.")
print("The word has", len(word_to_guess), "letters.")

def display_word():
    return " ".join(word_display)

attempts_left = max_attempts
while attempts_left > 0:
    print("\nWord:", display_word())
    print(f"Attempts remaining: {attempts_left}")
    
    guess = input("Enter a single letter: ").lower()

    if len(guess) != 1 or guess not in string.ascii_lowercase:
        print("Invalid input. Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        print("Good guess!")
        for i, char in enumerate(word_to_guess):
            if char == guess:
                word_display[i] = guess
                correct_letters.add(guess)
        if "_" not in word_display:
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    else:
        print("Wrong guess.")
        attempts_left -= 1

else:
    print("\nSorry, you've run out of attempts. The word was:", word_to_guess)
