#!/usr/bin/env python3
"""
Verify deployment package has all required files
"""

import os
import sys

def check_deployment_files():
    """Check that all required files are present"""
    print("🔍 Verifying Deployment Package")
    print("=" * 40)
    
    required_files = [
        "app.py",
        "requirements.txt", 
        "Procfile",
        "runtime.txt",
        "railway.json",
        "templates/index.html"
    ]
    
    all_good = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING!")
            all_good = False
    
    # Check templates folder specifically
    if os.path.exists("templates") and os.path.isdir("templates"):
        print("✅ templates/ directory exists")
        template_files = os.listdir("templates")
        if "index.html" in template_files:
            print("✅ templates/index.html found")
        else:
            print("❌ templates/index.html missing!")
            all_good = False
    else:
        print("❌ templates/ directory missing!")
        all_good = False
    
    print("\n" + "=" * 40)
    if all_good:
        print("🎉 Deployment package is complete!")
        print("Ready to upload to GitHub and deploy!")
    else:
        print("❌ Some files are missing. Please fix before deploying.")
    
    return all_good

if __name__ == "__main__":
    success = check_deployment_files()
    sys.exit(0 if success else 1) 