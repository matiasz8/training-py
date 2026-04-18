"""
Example: Secrets Management Introduction
Demonstrates basic secret handling and environment loading.
"""
import os


def main():
    """
    Load and use secrets from environment variables safely.
    """
    # In practice, these would be set via environment
    os.environ["DATABASE_PASSWORD"] = "secure-password-123"
    os.environ["API_KEY"] = "sk-1234567890"
    
    # Retrieve secrets
    db_password = os.getenv("DATABASE_PASSWORD")
    api_key = os.getenv("API_KEY")
    
    # Never print actual secrets in production
    if db_password and api_key:
        print("✅ Secrets loaded from environment")
        print(f"   Database: connected")
        print(f"   API: authenticated")
    else:
        print("❌ Required secrets not found")


if __name__ == "__main__":
    main()
