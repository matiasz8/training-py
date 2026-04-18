"""
Example: Package Tampering - Checksum Verification
Demonstrates detecting if packages have been modified or corrupted.
"""
import hashlib


def main():
    """
    Verify package integrity using checksums.
    """
    # Simulated package file content
    package_content = b"example-package-v1.0.0-source-code"
    
    # Calculate SHA256 checksum
    calculated_checksum = hashlib.sha256(package_content).hexdigest()
    
    # Expected checksum (as provided by official source)
    expected_checksum = hashlib.sha256(package_content).hexdigest()
    
    print(f"Calculated checksum: {calculated_checksum}")
    print(f"Expected checksum:   {expected_checksum}")
    
    if calculated_checksum == expected_checksum:
        print("✅ Package integrity verified - no tampering detected")
    else:
        print("❌ Checksum mismatch - package may be compromised")


if __name__ == "__main__":
    main()
