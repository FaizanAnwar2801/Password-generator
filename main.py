
from PasswordManager import PasswordManager

def main():
    manager = PasswordManager()

    # Generates passwords
    password_low = manager.generate_password(level="low")
    password_medium = manager.generate_password(level="medium")
    password_high = manager.generate_password(level="high")

    # Stores passwords
    manager.store_password("Facebook", "user123", password_medium)
    manager.store_password("Gmail", "user456", password_high)
    manager.store_password("Twitter", "user789", password_low)
    
    # Retrieves passwords
    print("Facebook Password:", manager.retrieve_password("Facebook"))
    print("Gmail Password:", manager.retrieve_password("Gmail"))
    print("Twitter Password:", manager.retrieve_password("Twitter"))
if __name__ == "__main__":
    main()
