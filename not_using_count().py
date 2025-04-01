# Prompt user for input
user_input = input("Enter a string: ")
# Prompt user for substring to count
substring = input("Enter the substring to count: ")
# Initialize count to 0
count = 0
# Loop through the string to find the substring
for i in range(len(user_input) - len(substring) + 1):
# Check if the substring is found
    if user_input[i:i + len(substring)] == substring:
# Increment count if found
        count += 1
# Print the count of occurrences of the substring