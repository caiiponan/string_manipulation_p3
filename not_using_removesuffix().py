# Prompt user for input
user_input = input("Enter a string: ")

# Ask user for suffix to remove
remove_suffix = input("Enter the suffix to remove: ")

# Check if the string ends with the specified suffix
if user_input.endswith(remove_suffix):
    result = user_input[:len(user_input) - len(remove_suffix)]

# Print result with removed suffix
