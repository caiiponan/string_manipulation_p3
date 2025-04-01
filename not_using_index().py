# Prompt user for input
user_input = input("Enter a string: ")
# Prompt user to input substring to find
substring = input("Enter the substring to find: ")

# Initialize default index to -1
index = -1

# Loop through the string to find the substring
for i in range(len(user_input) - len(substring) + 1):
# Check if the substring is found
    if user_input[i:i + len(substring)] == substring:
        index = i
        break
# Print the index of the substring