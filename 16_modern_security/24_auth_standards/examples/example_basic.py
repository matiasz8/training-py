"""
Example: Auth Standards - Authentication Types
Demonstrates different authentication standards.
"""
from enum import Enum


def main():
    """
    Define and use different authentication methods.
    """
    class AuthMethod(Enum):
        BASIC = "basic"
        BEARER = "bearer"
        API_KEY = "api_key"
        OAUTH2 = "oauth2"
        SAML = "saml"
    
    print("Supported Authentication Methods:")
    for auth_type in AuthMethod:
        print(f"  ✅ {auth_type.name}: {auth_type.value}")
    
    # Select auth method for connection
    selected_auth = AuthMethod.BEARER
    print(f"\n  Selected: {selected_auth.name} authentication")


if __name__ == "__main__":
    main()
