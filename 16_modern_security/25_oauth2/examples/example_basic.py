"""
Example: OAuth 2.0 - Token Flow
Demonstrates OAuth 2.0 authorization flow simulation.
"""


def main():
    """
    Simulate OAuth 2.0 authorization code flow.
    """
    # OAuth 2.0 configuration
    oauth_config = {
        "client_id": "app-client-123",
        "client_secret": "secret-xyz",
        "redirect_uri": "https://app.example.com/callback",
        "authorization_endpoint": "https://provider.com/oauth/authorize",
        "token_endpoint": "https://provider.com/oauth/token"
    }
    
    print("OAuth 2.0 Authorization Flow:")
    print(f"  1. Redirect to: {oauth_config['authorization_endpoint']}")
    print(f"  2. Client ID: {oauth_config['client_id']}")
    print(f"  3. Redirect URI: {oauth_config['redirect_uri']}")
    
    # Simulate token exchange
    auth_code = "auth_code_abc123"
    access_token = "access_token_xyz789"
    
    print(f"\n  ✅ Authorized with auth code: {auth_code[:10]}...")
    print(f"  ✅ Access token obtained: {access_token[:12]}...")


if __name__ == "__main__":
    main()
