# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

full_name = input("Please enter your name: ")
first_name = full_name.split()[0]

welcome = f"Hello!! {first_name}, is so nice you are here and \
you can join me in this exersice, I thank you for beign this nice. \
Have a nice day!!"

print(welcome)

