# Take user input
user_password = input("Enter password to check: ")

# Define functions we need
length_pass = len(user_password) >= 8
is_digits = any(char.isdigit() for char in user_password)
is_upper = any(char.isupper() for char in user_password)
special_char = any(not char.isalnum() for char in user_password)

# Set the conditions
score = 0
if length_pass:
    score += 1
if is_digits:
    score += 1
if is_upper:
    score += 1
if special_char:
    score += 1

# Give the verdict
if score == 4:
    print("Very strong password!")
elif score == 3:
    print("Strong password!")
elif score == 2:
    print("Medium password!")
else:
    print("Weak password! Please change your password!")
