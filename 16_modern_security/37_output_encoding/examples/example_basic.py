"""
Example: Output Encoding - Safe Data Encoding
Demonstrates encoding output data safely for different contexts.
"""
import html
import json


def main():
    """
    Encode output data for safe display in different contexts.
    """
    data = 'Hello & "World" <script>alert("XSS")</script>'
    
    print("Output Encoding:")
    
    # HTML context
    html_encoded = html.escape(data)
    print(f"  HTML encoded: {html_encoded}")
    
    # JSON context
    json_encoded = json.dumps(data)
    print(f"  JSON encoded: {json_encoded}")
    
    # URL context (simple example)
    url_encoded = data.replace(" ", "%20").replace("&", "%26")
    print(f"  URL encoded: {url_encoded}")
    
    print("\n  ✅ Output safely encoded for context")


if __name__ == "__main__":
    main()
