# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    vowel_counts = {vowel: 0 for vowel in vowels}

    for char in input_string.lower():
        if char in vowel_counts:
            vowel_counts[char] += 1

    print("Vowel counts:")
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")

user_input = input("Enter a string: ")
count_vowels(user_input)
