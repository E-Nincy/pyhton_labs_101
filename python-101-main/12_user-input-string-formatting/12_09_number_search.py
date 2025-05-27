# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

target = int(input("Enter a number between 0 and 1,000,000,000: "))

guess = 0

while guess != target:
    guess += 1

print(f"Found the number: {guess}")