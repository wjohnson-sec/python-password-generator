import random
import string

def generate_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for input
try:
    length = int(input("Enter desired password length (e.g., 12): "))
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_special)
    print(f"\nGenerated password: {password}")

except ValueError:
    print("Please enter a valid number for the password length.")
