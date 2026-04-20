"""
Example: Supply Chain Security - Validating Package Sources
Demonstrates how to verify package manifest and source integrity.
"""


def main():
    """
    Parse and validate package manifest metadata.
    Simulates checking package source integrity.
    """
    # Sample package manifest
    manifest = {
        "name": "example-package",
        "version": "1.0.0",
        "source": "https://github.com/example/package",
        "checksum": "sha256:abc123",
        "published_date": "2024-01-01",
    }

    # Validate manifest structure
    required_fields = ["name", "version", "source", "checksum"]
    missing = [f for f in required_fields if f not in manifest]

    if missing:
        print(f"Missing fields: {missing}")
    else:
        print(f"✅ Manifest valid for: {manifest['name']} v{manifest['version']}")
        print(f"   Source: {manifest['source']}")
        print(f"   Checksum: {manifest['checksum']}")


if __name__ == "__main__":
    main()
