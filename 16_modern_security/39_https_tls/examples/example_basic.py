"""
Example: HTTPS/TLS - Certificate Verification
Demonstrates TLS certificate verification.
"""


def main():
    """
    Verify TLS certificates for secure connections.
    """
    # Simulated certificate information
    certificate = {
        "subject": "CN=example.com",
        "issuer": "CN=Let's Encrypt Authority",
        "not_before": "2024-01-01",
        "not_after": "2025-01-01",
        "fingerprint": "sha256:abc123def456..."
    }
    
    print("TLS Certificate Verification:")
    print(f"  Domain: {certificate['subject']}")
    print(f"  Issuer: {certificate['issuer']}")
    print(f"  Valid from: {certificate['not_before']}")
    print(f"  Valid until: {certificate['not_after']}")
    
    # Check validity
    from datetime import datetime
    not_after = datetime.fromisoformat(certificate['not_after'])
    is_valid = not_after > datetime.now()
    
    if is_valid:
        print("  ✅ Certificate is valid")
    else:
        print("  ❌ Certificate is expired")


if __name__ == "__main__":
    main()
