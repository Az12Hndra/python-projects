# Import random library
import random
import time
import string

print('PASSWORD GENERATOR')
print('------------------')

# Take user input as their name will be changed into a password
user_name = input('Enter your name: ')
username_list = list(user_name)
random.shuffle(username_list)
shuffled_name = ''.join(username_list)

time.sleep(3)
print("Generating a password...")

time.sleep(3)

# Define functions
list_digits = '1234567890'
digits = ''.join(random.sample(list_digits, 3))
new_digits = str(digits)

list_special = '!@#$%&*?'
special = str(random.choice(list_special))

list_uppercase = string.ascii_uppercase
uppercase = str(random.choice(list_uppercase))

new_password = list(shuffled_name + special + uppercase + new_digits)
random.shuffle(new_password)
shuffled_password = ''.join(new_password)

print('')
print(f'Username: {user_name}')
print(f'Password: {shuffled_password}')