"""
Example: XSS/CSRF Prevention - Content Security Policy
Demonstrates implementing comprehensive CSP policies.
"""


def main():
    """
    Configure Content Security Policy for XSS/CSRF prevention.
    """
    csp_policies = {
        "default-src": ["'self'"],
        "script-src": ["'self'", "https://cdn.example.com"],
        "style-src": ["'self'", "'unsafe-inline'"],
        "img-src": ["'self'", "data:", "https:"],
        "connect-src": ["'self'", "https://api.example.com"],
        "font-src": ["'self'", "https://fonts.googleapis.com"],
        "frame-ancestors": ["'none'"],
        "base-uri": ["'self'"],
        "form-action": ["'self'"],
    }

    # Build CSP header value
    csp_header = "; ".join(
        f"{directive} {' '.join(sources)}" for directive, sources in csp_policies.items()
    )

    print("Content Security Policy:")
    print(f"  {csp_header[:80]}...")

    print("\nCSP Rules:")
    for directive, sources in csp_policies.items():
        print(f"  {directive}: {', '.join(sources)}")

    print("\n  ✅ CSP configured to prevent XSS/CSRF")


if __name__ == "__main__":
    main()
