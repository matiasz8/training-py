"""
Example: Software Licensing - License Extraction
Demonstrates extracting and identifying licenses from packages.
"""


def main():
    """
    Extract license information from packages.
    """
    packages = {
        "requests": "Apache-2.0",
        "django": "BSD-3-Clause",
        "flask": "BSD-3-Clause",
        "numpy": "BSD-3-Clause"
    }
    
    license_count = {}
    for package, license_type in packages.items():
        license_count[license_type] = license_count.get(license_type, 0) + 1
        print(f"📦 {package}: {license_type}")
    
    print("\nLicense Summary:")
    for license_type, count in license_count.items():
        print(f"  {license_type}: {count} packages")


if __name__ == "__main__":
    main()
