"""
Example: OpenID Connect - Identity Verification
Demonstrates OpenID Connect identity verification.
"""
import json


def main():
    """
    Verify OpenID Connect identity tokens.
    """
    # Simulated ID token payload
    id_token_payload = {
        "iss": "https://provider.example.com",
        "sub": "user-123",
        "aud": "client-app",
        "exp": 1234567890,
        "iat": 1234564290,
        "email": "user@example.com",
        "email_verified": True
    }
    
    print("OpenID Connect Identity Token:")
    print(f"  Issuer: {id_token_payload['iss']}")
    print(f"  Subject: {id_token_payload['sub']}")
    print(f"  Email: {id_token_payload['email']}")
    print(f"  Email Verified: {id_token_payload['email_verified']}")
    
    if id_token_payload['email_verified']:
        print("  ✅ Identity verified")
    else:
        print("  ❌ Email not verified")


if __name__ == "__main__":
    main()
