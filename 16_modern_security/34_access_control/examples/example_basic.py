"""
Example: Access Control - Permission Checking
Demonstrates access control and permission validation.
"""
from enum import Enum


def main():
    """
    Check user permissions before allowing access.
    """
    class Permission(Enum):
        READ = "read"
        WRITE = "write"
        DELETE = "delete"
        ADMIN = "admin"
    
    # Simulated user permissions
    user_permissions = {
        "user1": [Permission.READ, Permission.WRITE],
        "admin": [Permission.READ, Permission.WRITE, Permission.DELETE, Permission.ADMIN]
    }
    
    def check_access(user, action):
        user_perms = user_permissions.get(user, [])
        return action in user_perms
    
    print("Access Control Check:")
    print(f"  user1 can READ: {'✅' if check_access('user1', Permission.READ) else '❌'}")
    print(f"  user1 can DELETE: {'✅' if check_access('user1', Permission.DELETE) else '❌'}")
    print(f"  admin can DELETE: {'✅' if check_access('admin', Permission.DELETE) else '❌'}")


if __name__ == "__main__":
    main()
