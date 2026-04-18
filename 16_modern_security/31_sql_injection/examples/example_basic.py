"""
Example: SQL Injection - Parameterized Queries
Demonstrates protection against SQL injection.
"""


def main():
    """
    Use parameterized queries to prevent SQL injection.
    """
    # Simulated parameterized query
    user_id = "1' OR '1'='1"  # Malicious input
    
    # ❌ UNSAFE: Direct string concatenation
    unsafe_query = f"SELECT * FROM users WHERE id = {user_id}"
    print("❌ Unsafe query (vulnerable):")
    print(f"   {unsafe_query}")
    
    # ✅ SAFE: Parameterized query
    safe_query = "SELECT * FROM users WHERE id = ?"
    safe_params = (user_id,)
    print("\n✅ Safe parameterized query:")
    print(f"   Query: {safe_query}")
    print(f"   Params: {safe_params}")
    print("\n   Parameter binding prevents injection")


if __name__ == "__main__":
    main()
