#Random Password Generator
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Define possible character sets based on user preferences
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        character_set += string.digits         # 0-9
    if use_symbols:
        character_set += string.punctuation    # !@#$%^&*() etc.

    # Ensure that at least one character type is selected
    if not character_set:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password using the selected character set
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    # Get user input for password criteria
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
