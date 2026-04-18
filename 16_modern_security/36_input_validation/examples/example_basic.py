"""
Example: Input Validation - Data Type Checking
Demonstrates validating input data types and formats.
"""
import re


def main():
    """
    Validate user input against expected formats.
    """
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_age(age):
        try:
            age_int = int(age)
            return 0 <= age_int <= 150
        except ValueError:
            return False
    
    # Test inputs
    test_cases = {
        "email@example.com": "email",
        "invalid-email": "email",
        "25": "age",
        "200": "age",
        "not_a_number": "age"
    }
    
    print("Input Validation:")
    for test_value, test_type in test_cases.items():
        if test_type == "email":
            result = validate_email(test_value)
        elif test_type == "age":
            result = validate_age(test_value)
        
        status = "✅" if result else "❌"
        print(f"  {status} {test_value} ({test_type})")


if __name__ == "__main__":
    main()
