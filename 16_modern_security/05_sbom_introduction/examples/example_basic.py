"""
Example: SBOM Introduction - Software Bill of Materials
Demonstrates creating a basic Software Bill of Materials structure.
"""
import json
from datetime import datetime


def main():
    """
    Create and display a basic SBOM structure.
    """
    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.4",
        "version": 1,
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "tools": [{"name": "sbom-generator", "version": "1.0.0"}],
        },
        "components": [
            {
                "type": "library",
                "name": "requests",
                "version": "2.31.0",
                "purl": "pkg:pypi/requests@2.31.0",
            },
            {
                "type": "library",
                "name": "django",
                "version": "4.2.0",
                "purl": "pkg:pypi/django@4.2.0",
            },
        ],
    }

    print("SBOM Generated:")
    print(json.dumps(sbom, indent=2))


if __name__ == "__main__":
    main()
