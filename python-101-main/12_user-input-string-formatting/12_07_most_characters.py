# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

# Take three strings as input from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str3 = input("Enter third string: ")

strings = [str1, str2, str3]

longest = max(strings, key=len)

print(f"{len(longest)}, {longest}")
