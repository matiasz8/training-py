"""
Example: Artifact Signing - HMAC Signatures
Demonstrates creating and verifying artifact signatures.
"""
import hmac
import hashlib


def main():
    """
    Sign an artifact and verify its signature.
    """
    # Secret key for signing
    secret_key = b"my-secret-signing-key"
    
    # Artifact content
    artifact = b"v1.0.0-application-package"
    
    # Create signature
    signature = hmac.new(secret_key, artifact, hashlib.sha256).hexdigest()
    print(f"Artifact: {artifact.decode()}")
    print(f"Signature: {signature}")
    
    # Verify signature
    expected_signature = hmac.new(secret_key, artifact, hashlib.sha256).hexdigest()
    
    if signature == expected_signature:
        print("✅ Signature verified - artifact is authentic")
    else:
        print("❌ Signature mismatch - artifact may be tampered")


if __name__ == "__main__":
    main()
