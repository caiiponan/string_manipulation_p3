# Prompt user for input
user_input = input("Enter a string: ")
# Prompt user for width
width = int(input("Enter the width: "))

# Check for padding
padding_length = width - len(user_input)

# If padding is needed, add spaces to the left to fit width given
# Print result with added zeroes