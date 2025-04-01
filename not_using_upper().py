# Let user input a string
user_input = input("Enter a string: ")

# Initialize an empty string 'uppercase_text' to store the result.
uppercase_text = ""

# Loop through each character in user input.
for char in user_input:
    if 'a' <= char <= 'z':# If the character is a lowercase letter (between 'a' and 'z')
        uppercase_text += chr(ord(char) - 32) # Convert it to uppercase by subtracting 32 from its ASCII value.
    else: # If the character is not a lowercase letter:
        uppercase_text += char# Append it to 'uppercase_text' as it is.

# Print the original and uppercase converted strings.