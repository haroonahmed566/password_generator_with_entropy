import secrets
import string
import math
import argparse
import pyperclip

def generate_password(length: int = 14, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))


def calculate_entropy(length, charset_size):
    return round(length * math.log2(charset_size), 2)

def main():
    parser = argparse.ArgumentParser(description="Password Generator with Entropy Calculation")
    parser.add_argument("-l", "--length", type=int, default=14, help="Password length")
    parser.add_argument("-nd", "--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("-ns", "--no-special", action="store_true", help="Exclude special characters")
    parser.add_argument("-e", "--entropy", action="store_true", help="Calculate entropy")
    args = parser.parse_args()

    length = args.length
    use_digits = not args.no_digits
    use_special_chars = not args.no_special


    charset_size = len(string.ascii_letters) + (len(string.digits) if use_digits else 0) + (len(string.punctuation) if use_special_chars else 0)

    password = generate_password(length, use_digits, use_special_chars)
    entropy = calculate_entropy(length, charset_size)


    print("Generated Password:", password)
    pyperclip.copy(password)
    print("Password copied to clipboard")
    if args.entropy:
        print("Generated Password's entropy score:", entropy)

if __name__ == "__main__":
    main()