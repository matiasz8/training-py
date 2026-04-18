"""
Example: CSRF Protection - Token Generation
Demonstrates CSRF token generation and validation.
"""
import secrets
import hashlib


def main():
    """
    Generate and validate CSRF tokens.
    """
    # Generate CSRF token
    csrf_token = secrets.token_urlsafe(32)
    print(f"CSRF Token generated: {csrf_token[:20]}...")
    
    # Store token in session (simulated)
    session_token = csrf_token
    
    # Verify token from request matches session
    request_token = csrf_token  # In real scenario, from request
    
    if secrets.compare_digest(session_token, request_token):
        print("✅ CSRF token validation successful")
    else:
        print("❌ CSRF token mismatch - request rejected")
    
    # Show token in form would look like
    print(f"\n  Hidden form field:")
    print(f'  <input type="hidden" name="csrf_token" value="{csrf_token[:20]}...">')


if __name__ == "__main__":
    main()
