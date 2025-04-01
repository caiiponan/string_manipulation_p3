# Prompt user for input
user_input = input("Enter a string: ")

# Let user input prefix to check
prefix = input("Enter the prefix to check: ")

# Assume string starts with prefix
starts_with = True

# Loop trough each character in the prefix
# Check if we reach the end of the text or if characters do not match
# If the prefix is not found, set the result to False
# Print result