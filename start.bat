@echo off
echo ===============================================
echo Academic Video Finder
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if app.py exists
if not exist "app.py" (
    echo Error: app.py not found
    echo Please run this batch file from the project directory
    pause
    exit /b 1
)

REM Install dependencies if not already installed
echo Installing dependencies...
pip install -r requirements.txt

REM Create uploads directory if it doesn't exist
if not exist "uploads" mkdir uploads

echo.
echo Starting the Academic Video Finder...
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

REM Start the Flask application
python app.py

echo.
echo Server stopped.
pause
