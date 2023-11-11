#!/bin/bash

source venv/bin/activate

pip install pyinstaller

pyinstaller --onefile main.py

cp -r resources dist
cp config.txt dist

mv dist/main dist/autofisher
mv dist autofisher

tar -czvf autofisher.tar.gz autofisher