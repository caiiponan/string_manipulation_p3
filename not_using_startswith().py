# Prompt user for input
user_input = input("Enter a string: ")

# Let user input prefix to check
prefix = input("Enter the prefix to check: ")

# Assume string starts with prefix
starts_with = True

# Loop trough each character in the prefix
for i in range(len(prefix)):

# Check if we reach the end of the text or if characters do not match
    if i >= len(user_input) or user_input[i] != prefix[i]:
# If the prefix is not found, set the result to False
        starts_with = False
        break
# Print result