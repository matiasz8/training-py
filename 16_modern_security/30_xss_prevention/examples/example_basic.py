"""
Example: XSS Prevention - HTML Escaping
Demonstrates HTML escaping to prevent XSS attacks.
"""
import html


def main():
    """
    Escape potentially dangerous HTML content.
    """
    # User input that could contain malicious script
    user_input = '<script>alert("XSS Attack")</script>'
    
    # Escape HTML entities
    safe_output = html.escape(user_input)
    
    print("XSS Prevention - HTML Escaping:")
    print(f"  Original input: {user_input}")
    print(f"  Escaped output: {safe_output}")
    
    # Show rendering
    print("\n  Safe HTML rendering:")
    print(f'  <div>{safe_output}</div>')
    print("  ✅ Input safely escaped")


if __name__ == "__main__":
    main()
