import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length < 4:
        print("Password length should be at least 4 for decent strength.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")

    while True:
        try:
            length = int(input("\nEnter desired password length: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_upper, use_digits, use_symbols)
        if password:
            print(f"\nGenerated Password: {password}")

        again = input("\nGenerate another password? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    password_generator()
