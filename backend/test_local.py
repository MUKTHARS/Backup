#!/usr/bin/env python3
"""
Test local development setup
"""
import requests
import json

BASE_URL = "http://localhost:8080/api"

def test_endpoints():
    print("Testing local endpoints...")
    
    # Test 1: Health endpoint
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✓ Health endpoint: {response.status_code}")
    except Exception as e:
        print(f"✗ Health endpoint failed: {e}")
    
    # Test 2: Login status (should work without auth)
    try:
        response = requests.get(f"{BASE_URL}/auth/login-status")
        print(f"✓ Login status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"  Authenticated: {data.get('authenticated', False)}")
    except Exception as e:
        print(f"✗ Login status failed: {e}")
    
    print("\nTo test login, use these test credentials:")
    print("Email: test@example.com")
    print("Password: test123")
    print("\nOr register a new account")

if __name__ == "__main__":
    test_endpoints()