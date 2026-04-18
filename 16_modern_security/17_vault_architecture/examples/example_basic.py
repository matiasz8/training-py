"""
Example: Vault Architecture - KV Operations
Demonstrates Vault key-value store operations.
"""


def main():
    """
    Simulate Vault KV store read/write operations.
    """
    # Simulated Vault KV store
    kv_store = {}
    
    # Write operation
    path = "secret/database/prod"
    secret_data = {
        "username": "admin",
        "password": "secure-db-password"
    }
    
    kv_store[path] = secret_data
    print(f"✅ Written to {path}")
    
    # Read operation
    if path in kv_store:
        retrieved = kv_store[path]
        print(f"✅ Retrieved secret from {path}")
        print(f"   Keys: {', '.join(retrieved.keys())}")
    else:
        print(f"❌ Secret not found at {path}")


if __name__ == "__main__":
    main()
