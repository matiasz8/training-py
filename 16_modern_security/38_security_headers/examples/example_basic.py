"""
Example: Security Headers - Header Configuration
Demonstrates setting security headers in HTTP responses.
"""


def main():
    """
    Configure security headers to protect web applications.
    """
    security_headers = {
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Content-Security-Policy": "default-src 'self'",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    
    print("Security Headers Configuration:")
    for header, value in security_headers.items():
        print(f"  {header}:")
        print(f"    {value}")
    
    print("\n  ✅ Security headers configured")


if __name__ == "__main__":
    main()
