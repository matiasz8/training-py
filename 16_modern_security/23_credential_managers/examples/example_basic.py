"""
Example: Credential Managers - Password Storage
Demonstrates password storage and retrieval patterns.
"""


def main():
    """
    Simulate secure credential management.
    """
    # Simulated credential store
    credentials = {
        "github": {
            "username": "developer",
            "token": "***"
        },
        "docker": {
            "username": "user",
            "password": "***"
        }
    }
    
    print("Credential Manager:")
    print("  Stored credentials:")
    for service, creds in credentials.items():
        print(f"    {service}: {'✅ stored' if creds else '❌ missing'}")
    
    # Retrieve credential safely
    try:
        github_creds = credentials.get("github")
        if github_creds:
            print(f"  ✅ Retrieved GitHub credentials")
    except Exception as e:
        print(f"  ❌ Error retrieving credentials: {e}")


if __name__ == "__main__":
    main()
