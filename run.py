#!/usr/bin/env python3
"""
Academic Video Finder - Simple startup script
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if all required dependencies are installed"""
    try:
        import flask
        import PyPDF2
        import pptx
        import youtube_search
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    print("=" * 50)
    print("Academic Video Finder")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("✗ app.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        print("✓ Created uploads directory")
    
    print("✓ Starting the application...")
    print("✓ Open your browser and go to: http://localhost:5000")
    print("✓ Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Start the Flask application
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n✓ Server stopped successfully")
    except Exception as e:
        print(f"✗ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
