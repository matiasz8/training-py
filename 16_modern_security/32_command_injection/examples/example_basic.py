"""
Example: Command Injection - Safe Command Building
Demonstrates protection against command injection.
"""
import shlex


def main():
    """
    Build commands safely to prevent injection.
    """
    # User input
    user_filename = "file.txt; rm -rf /"  # Malicious input
    
    # ❌ UNSAFE: Using shell=True with string
    unsafe_command = f"cat {user_filename}"
    print("❌ Unsafe command (shell=True with concatenation):")
    print(f"   {unsafe_command}")
    
    # ✅ SAFE: Using list form without shell
    safe_command = ["cat", user_filename]
    print("\n✅ Safe command (using list form):")
    print(f"   {safe_command}")
    print("\n   List form prevents shell interpretation")
    
    # Alternative: proper escaping
    escaped = shlex.quote(user_filename)
    print(f"\n✅ Safe with escaping: cat {escaped}")


if __name__ == "__main__":
    main()
