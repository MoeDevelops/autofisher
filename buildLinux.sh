#!/bin/bash

source venv/bin/activate

pip install pyinstaller

pyinstaller --onefile main.py

cp -r resources dist
cp config.txt dist
cp README.md dist

mv dist/main dist/autofisher
mv dist autofisher

tar -czvf autofisher_linux_x64.tar.gz autofisher