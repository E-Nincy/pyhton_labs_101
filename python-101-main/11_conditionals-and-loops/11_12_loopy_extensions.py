# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

length = 0
for _ in filename:
    length += 1

# I start with False because I haven’t found anything yet.
dot_ok = False
p_ok = False
d_ok = False
f_ok = False

position = 0
for char in filename:
    if position == length - 4 and char == '.':
        dot_ok = True
    if position == length - 3 and char == 'p':
        p_ok = True
    if position == length - 2 and char == 'd':
        d_ok = True
    if position == length - 1 and char == 'f':
        f_ok = True
    position += 1

# Result
if dot_ok and p_ok and d_ok and f_ok:
    print("This is a .pdf file.")
else:
    print("This is NOT a .pdf file.")
