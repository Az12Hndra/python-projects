# Take user input
password = input("Enter to check your password: ")

# Define functions that you will use
length = len(password) >= 8
digits = any(char.isdigit() for char in password) 
upper = any(char.isupper() for char in password)

# Set the conditions
score = 0
if length:
    score += 1

if digits:
    score += 1

if upper:
    score += 1

# Give the verdict
if score == 3:
    print("Strong password!")
elif score == 2:
    print("Medium password!")
else:
    print("Weak password! Please consider to change password immediately!")
