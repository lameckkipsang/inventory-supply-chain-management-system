import re

def validate_email_address(email_input):
    """Uses regular expressions to check if a supplier email is in a valid format."""
    email_pattern = r"[\w.-]+@[\w.-]+\.\w+"
    match_result = re.search(email_pattern, email_input)
    if match_result:
        return True
    else:
        return False

def get_valid_integer(prompt_message):
    """Ensures the user inputs a valid integer, handling exceptions to prevent crashing."""
    while True:
        user_input = input(prompt_message)
        try:
            valid_integer = int(user_input)
            return valid_integer
        except ValueError:
            print("Error: Please enter a valid numerical value.")

def verify_admin_authorization():
    """Prompts the user for an admin password to authorize sensitive operations."""
    ADMIN_PASSWORD = "admin"
    attempts = 3
    
    while attempts > 0:
        entered_password = input("Enter Admin Authorization Password: ")
        if entered_password == ADMIN_PASSWORD:
            print("Authorization successful.")
            return True
        attempts -= 1
        print(f"Access Denied. Incorrect password. ({attempts} attempts remaining)")
        
    return False