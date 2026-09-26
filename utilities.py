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