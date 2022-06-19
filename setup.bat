python -m pip install -r requirements.txt
cls
echo python group_locker.py >> start.bat
start start.bat
start /b "" cmd /c &exit /b
