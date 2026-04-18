"""
Example: License Compliance - Checking Compatibility
Demonstrates verifying license compatibility in projects.
"""


def main():
    """
    Check license compatibility for a project.
    """
    # Acceptable licenses for this project
    acceptable_licenses = [
        "MIT",
        "Apache-2.0",
        "BSD-3-Clause",
        "ISC"
    ]
    
    # Project dependencies with licenses
    dependencies = {
        "requests": "Apache-2.0",
        "django": "BSD-3-Clause",
        "proprietary-lib": "Proprietary"
    }
    
    print("Checking license compliance:")
    for package, license_type in dependencies.items():
        if license_type in acceptable_licenses:
            print(f"✅ {package}: {license_type} - COMPLIANT")
        else:
            print(f"❌ {package}: {license_type} - NOT COMPLIANT")


if __name__ == "__main__":
    main()
