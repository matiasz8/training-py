"""
Example: CycloneDX - Dependency Tree Parsing
Demonstrates parsing and navigating CycloneDX component hierarchies.
"""
import json


def main():
    """
    Parse a CycloneDX SBOM with nested dependencies.
    """
    cyclonedx_sbom = {
        "bomFormat": "CycloneDX",
        "components": [
            {
                "name": "django",
                "version": "4.2.0",
                "dependencies": [
                    {"name": "sqlparse", "version": "0.4.4"},
                    {"name": "tzdata", "version": "2024.1"}
                ]
            }
        ]
    }
    
    print("Parsing CycloneDX SBOM:")
    for component in cyclonedx_sbom["components"]:
        print(f"\n📦 {component['name']} v{component['version']}")
        if "dependencies" in component:
            print("   Dependencies:")
            for dep in component["dependencies"]:
                print(f"     - {dep['name']} v{dep['version']}")


if __name__ == "__main__":
    main()
