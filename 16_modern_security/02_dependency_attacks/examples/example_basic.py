"""
Example: Dependency Attacks - Version Validation
Demonstrates protection against malicious or compromised dependencies.
"""
import re


def main():
    """
    Validate dependency versions to prevent attacks from outdated packages.
    """
    dependencies = {
        "requests": "2.31.0",
        "django": "4.2.0",
        "flask": "2.3.0"
    }
    
    # Define minimum secure versions
    min_versions = {
        "requests": "2.28.0",
        "django": "4.0.0",
        "flask": "2.0.0"
    }
    
    for package, installed_version in dependencies.items():
        min_required = min_versions.get(package, "0.0.0")
        
        # Simple version comparison
        installed_parts = [int(x) for x in installed_version.split('.')]
        required_parts = [int(x) for x in min_required.split('.')]
        
        if installed_parts >= required_parts:
            print(f"✅ {package} {installed_version} is secure")
        else:
            print(f"❌ {package} {installed_version} needs update to >= {min_required}")


if __name__ == "__main__":
    main()
