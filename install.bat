@echo off
echo ========================================
echo VOICE ASSISTANT SETUP
echo ========================================
echo.
echo This assistant works WITHOUT any Python
echo package installations!
echo.
echo Simply run the Python file directly.
echo.
pause

REM Create the Python file if it doesn't exist
if not exist "voice_assistant.py" (
    echo Creating voice_assistant.py...
    echo Please run the Python code manually
) else (
    echo Running voice_assistant.py...
    python voice_assistant.py
)

pause