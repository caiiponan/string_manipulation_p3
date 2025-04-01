# Prompt user for input
user_input = input("Enter a string: ")

# Prompt user for width
width = int(input("Enter the width: "))

# Calculate how many characters to add
space_length = width - len(user_input)

# Add spaces to the left to fit width given
# Print result with added spaces