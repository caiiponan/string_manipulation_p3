user_input = input("Enter a string: ") # Let user input a string
is_lowercase = True # Initialize a boolean variable 'is_lowercase' to True.

for char in user_input: # Iterate over each character in user input.
    if "A" <= char <= "Z": # Check if the character is an uppercase letter (between 'A' and 'Z')
        is_lowercase = False # is_lowercase = False if any character is uppercase.
        break

print(is_lowercase) # Print the result of the check.