# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

user_input = input("Write Hello World:")

for index, char in enumerate(user_input):
    if char == "o":
        print(index)