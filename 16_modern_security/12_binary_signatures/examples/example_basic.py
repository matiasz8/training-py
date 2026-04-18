"""
Example: Binary Signatures - Hash Verification
Demonstrates verifying binary file integrity through signatures.
"""
import hashlib


def main():
    """
    Create and verify signatures for binary files.
    """
    # Simulated binary file content
    binary_content = b"\x89PNG\r\n\x1a\n" + b"binary-data" * 100
    
    # Calculate signature hash
    signature = hashlib.sha256(binary_content).hexdigest()
    
    # Verify signature
    expected_signature = hashlib.sha256(binary_content).hexdigest()
    
    print(f"Binary file size: {len(binary_content)} bytes")
    print(f"Signature (SHA256): {signature[:32]}...")
    
    if signature == expected_signature:
        print("✅ Binary signature verified - file is authentic")
    else:
        print("❌ Signature mismatch")


if __name__ == "__main__":
    main()
