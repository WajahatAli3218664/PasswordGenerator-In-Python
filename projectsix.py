# Project 6: Password Generator In Python
# Description: This is a password generator that creates strong and random passwords using uppercase, lowercase, digits, and special characters.
# Instructor: Wajahat Ali

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User inputs
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Your Desired Generated Password:", password)
print("Password Length:", len(password))
