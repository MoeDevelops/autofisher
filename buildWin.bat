venv\Scripts\activate

pip install pyinstaller

xcopy resources\ dist\resources
copy config.txt dist

move dist\main.exe dist\autofisher.exe
rename dist autofisher

powershell Compress-Archive -Path autofisher -DestinationPath autofisher_win_x64.zip