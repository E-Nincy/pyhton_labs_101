# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

# Pick letters by index:
# word = "t w e e z e r s  "
#          0 1 2 3 4 5 6 7 8

sentence = word[1] + word[2] + " " + word[7] + word[2] + word[2] + word[8] + word[0] + word[6] + word[3] + word[3] + word[7]
print(sentence)
 #Output: we see trees
# The above code extracts the letters from the string "tweezers" using their respective indices to form the sentence "we see trees".
