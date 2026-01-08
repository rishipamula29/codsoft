
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if characters == "":
        return "Error: No character set selected."

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


print("====== PASSWORD GENERATOR ======")

# User input for password length
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Complexity options
print("\nSelect password complexity:")
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate password
password = generate_password(length, use_upper, use_lower, use_digits, use_special)

# Display password
print("\nGenerated Password:")
print(password)
