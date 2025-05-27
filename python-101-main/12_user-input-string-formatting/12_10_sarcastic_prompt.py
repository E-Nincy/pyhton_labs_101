# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_input = input("Give me your *honest* opinion: ")

# Convert to aLtErNaTiNg CaPs
sarcastic_output = ""
capitalize = True

for char in user_input:
    if char.isalpha():
        if capitalize:
            sarcastic_output += char.upper()
        else:
            sarcastic_output += char.lower()
        capitalize = not capitalize  # flip for next letter
    else:
        sarcastic_output += char 

print("Oh wow, you said:")
print(sarcastic_output)