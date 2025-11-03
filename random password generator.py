import secrets
import string

def generate_password(length=12):
    """Generate a strong random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    print("✨ Random Password Generator ✨")
    user_length = input("Enter password length (press Enter for 12): ")
    if user_length.strip() == "":
        user_length = 12
    else:
        user_length = int(user_length)
    print("\nYour secure password is:\n", generate_password(user_length))
