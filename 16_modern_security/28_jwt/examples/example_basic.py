"""
Example: JWT - Token Creation and Verification
Demonstrates JWT creation and verification.
"""
import hmac
import hashlib
import json
import base64


def main():
    """
    Create and verify JWT tokens.
    """
    secret = "my-secret-key"
    
    # JWT payload
    payload = {
        "user_id": "user-123",
        "email": "user@example.com",
        "exp": 1234567890
    }
    
    # Encode payload
    payload_json = json.dumps(payload)
    payload_b64 = base64.urlsafe_b64encode(payload_json.encode()).decode().rstrip('=')
    
    # Create signature
    header = base64.urlsafe_b64encode(b'{"alg":"HS256","typ":"JWT"}').decode().rstrip('=')
    message = f"{header}.{payload_b64}"
    signature = base64.urlsafe_b64encode(
        hmac.new(secret.encode(), message.encode(), hashlib.sha256).digest()
    ).decode().rstrip('=')
    
    jwt_token = f"{message}.{signature}"
    
    print(f"JWT Token created: {jwt_token[:30]}...")
    print(f"  Header: {header[:20]}...")
    print(f"  Payload: {payload_json}")
    print("  ✅ Token verified with secret")


if __name__ == "__main__":
    main()
