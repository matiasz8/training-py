"""
Example: Secret Rotation - Tracking Changes
Demonstrates secret rotation and version tracking.
"""
from datetime import datetime, timedelta


def main():
    """
    Track and manage secret rotation schedules.
    """
    now = datetime.now()
    rotation_period = 90  # days
    
    secrets_rotation = {
        "api_key": {
            "last_rotated": now - timedelta(days=30),
            "next_rotation": now + timedelta(days=60),
            "status": "current"
        },
        "db_password": {
            "last_rotated": now - timedelta(days=85),
            "next_rotation": now + timedelta(days=5),
            "status": "urgent"
        }
    }
    
    print("Secret Rotation Status:")
    for secret_name, info in secrets_rotation.items():
        days_until = (info["next_rotation"] - now).days
        print(f"  {secret_name}: {info['status']} ({days_until} days until rotation)")
        if days_until < 10:
            print(f"    ⚠️  Rotation needed soon")


if __name__ == "__main__":
    main()
