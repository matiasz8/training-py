"""
Example: Path Traversal - Path Normalization
Demonstrates protection against path traversal attacks.
"""
from pathlib import Path
import os


def main():
    """
    Safely normalize and validate file paths.
    """
    # Base directory for user files
    base_dir = Path("/app/user_files")
    
    # Malicious path with traversal attempt
    user_path = "../../etc/passwd"
    
    # ❌ UNSAFE: Direct concatenation
    unsafe_full_path = str(base_dir / user_path)
    print("❌ Unsafe path resolution (allows traversal):")
    print(f"   {unsafe_full_path}")
    
    # ✅ SAFE: Normalize and validate
    full_path = (base_dir / user_path).resolve()
    is_safe = str(full_path).startswith(str(base_dir.resolve()))
    
    print("\n✅ Safe path resolution:")
    print(f"   Resolved: {full_path}")
    print(f"   Within base_dir: {is_safe}")
    
    if is_safe:
        print("   ✅ Path is safe")
    else:
        print("   ❌ Path traversal detected - access denied")


if __name__ == "__main__":
    main()
