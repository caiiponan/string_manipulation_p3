# Prompt user for input
user_input = input("Enter a string: ")

# Check if the string is empty
index = len(user_input) - 1

# Iterate backwards through the string to find the last non-space character
# Check for trailing spaces
while index >= 0 and user_input[index] == ' ':
    index -= 1
# Return the string without trailing spaces
# Print the result without trailing spaces