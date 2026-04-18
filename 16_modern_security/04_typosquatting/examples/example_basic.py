"""
Example: Typosquatting - Package Name Validation
Demonstrates detection of malicious packages with similar names.
"""
import difflib


def main():
    """
    Detect potential typosquatting attempts by comparing package names.
    """
    legitimate_packages = ["requests", "django", "numpy", "pandas", "flask"]
    suspicious_packages = ["requets", "dajngo", "numphy", "panda", "flask"]
    
    for suspicious in suspicious_packages:
        # Calculate similarity with all legitimate packages
        matches = difflib.get_close_matches(suspicious, legitimate_packages, n=1, cutoff=0.6)
        
        if matches:
            print(f"⚠️  '{suspicious}' is similar to '{matches[0]}' - possible typosquatting")
        else:
            print(f"✅ '{suspicious}' has no close legitimate package matches")


if __name__ == "__main__":
    main()
