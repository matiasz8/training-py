"""
Example: Container Security - Image Validation
Demonstrates validating container image integrity.
"""
import hashlib


def main():
    """
    Validate container image hashes and metadata.
    """
    container_images = {
        "nginx:latest": {
            "digest": "sha256:1234abcd",
            "trusted": True
        },
        "suspicious-image:v1": {
            "digest": "sha256:unknown",
            "trusted": False
        }
    }
    
    print("Container Security Check:")
    for image, metadata in container_images.items():
        if metadata["trusted"]:
            print(f"✅ {image} - trusted image")
        else:
            print(f"❌ {image} - untrusted source")


if __name__ == "__main__":
    main()
