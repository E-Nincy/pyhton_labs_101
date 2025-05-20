# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
#   0         10        20        30        40        50        60       70       78

word1 = s[5:9] + s[11]  # 'grape'
word2 = s[57:63]    # 'butter'
word3 = s[63:67]   # 'cups'
word4 = s[68:73]   # 'flour'

print(word1, word2, word3, word4)

# Output: grape butter cups flour
# The dish you can make from these ingredients is "a grape pie in a cup"

