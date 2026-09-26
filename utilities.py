import re

def validate_email_address(email_input):
    """Uses regular expressions to check if a supplier email is in a valid format."""
    email_pattern = r"[\w.-]+@[\w.-]+\.\w+"
    match_result = re.search(email_pattern, email_input)
    if match_result:
        return True
    else:
        return False