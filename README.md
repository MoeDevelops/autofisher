# Minecraft Autofisher
This Python script automates fishing in Minecraft, specifically designed for open waters as AFK-fishing became less effective after Version 1.16, which restricted treasure acquisition in closed-off water bodies.

## How does it work
The script captures screenshots of the Minecraft screen, monitoring for the appearance of the "Fishing Bobber splashes" text in the subtitles. Upon detection, the script initiates two right-click actions with a delay, allowing you to reel in loot and cast your fishing rod again.

## Setup
### Linux
1. Set up a virtual environment (optional but recommend)
    ```bash
    python3 -m venv venv
    ```
2. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
3. Install dependencies
    ```bash
    pip install pyautogui pynput opencv-python
    ```
4. Rename the bobber image<br>
Look in the resources folder for the file with your GUI Scale.<br>
Then rename it to Bobber.png<br>
The default is a GUI Scale of 3x
5. Start the script
    ``` bash
    python3 autofisher.py
    ```

### Windows
1. Set up a virtual environment (optional but recommend)
    ```bash
    python3 -m venv venv
    ```
2. Activate the virtual environment
    ```bash
    venv\Scripts\activate
    ```
3. Install dependencies
    ```bash
    pip install pyautogui pynput opencv-python
    ```
4. Rename the bobber image<br>
Look in the resources folder for the file with your GUI Scale.<br>
Then rename it to Bobber.png<br>
The default is a GUI Scale of 3x
5. Start the script
    ``` bash
    python autofisher.py
    ```

## Notes
- This script has only been tested on Linux with Debian and KDE Plasma.
- **Caution:** The use of this script may be considered cheating on some servers. Please use it responsibly.