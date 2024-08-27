@echo off

:: Step 1: Install required packages
python -m pip install --upgrade pip
python -m pip install requests colorama pystyle aiohttp pyinstaller

:: Step 2: Generate the .exe file using PyInstaller
pyinstaller --onefile --name "Webhook Tool" --icon="logoBat.ico" webhookTool.py

echo Setup complete! The executable has been created.
pause