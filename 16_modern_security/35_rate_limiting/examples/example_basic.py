"""
Example: Rate Limiting - Request Counter
Demonstrates rate limiting to prevent abuse.
"""
from datetime import datetime, timedelta


def main():
    """
    Implement rate limiting for API requests.
    """
    # Rate limit: 100 requests per minute per IP
    rate_limit = 100
    time_window = 60  # seconds
    
    # Simulated request tracking
    request_log = {
        "192.168.1.1": [
            datetime.now() - timedelta(seconds=i)
            for i in range(50)
        ]
    }
    
    def is_rate_limited(ip_address):
        if ip_address not in request_log:
            return False
        
        now = datetime.now()
        cutoff = now - timedelta(seconds=time_window)
        
        recent_requests = [
            t for t in request_log[ip_address]
            if t > cutoff
        ]
        
        return len(recent_requests) >= rate_limit
    
    print("Rate Limiting Check:")
    test_ip = "192.168.1.1"
    if is_rate_limited(test_ip):
        print(f"  ❌ {test_ip} - RATE LIMITED")
    else:
        print(f"  ✅ {test_ip} - Request allowed")


if __name__ == "__main__":
    main()
