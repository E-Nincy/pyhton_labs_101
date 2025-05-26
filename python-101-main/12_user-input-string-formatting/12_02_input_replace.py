# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

user_input = input("Can you tell me something?:")
symbol = input("Enter a symbol to replace the first letter: ")

new_text = ""
first_letter = user_input[0]

for char in user_input:
    if char == first_letter:
        new_text += symbol
    else:
        new_text += char

print(new_text)