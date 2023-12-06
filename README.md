# Minecraft Autofisher
This Python script automates fishing in Minecraft, specifically designed for open waters as AFK-fishing became less effective after Version 1.16, which restricted treasure acquisition in closed-off water bodies.

## How does it work
The script captures screenshots of the Minecraft screen, monitoring for the appearance of the "Fishing Bobber splashes" text in the subtitles. Upon detection, the script initiates two right-click actions with a delay, allowing you to reel in loot and cast your fishing rod again.

## Configuration
### Minecraft
* Ensure you're not using a texture pack that changes the font.
* Check your GUI Scale setting. If it's set to Auto, configure it to a value you prefer.

### config.txt
* Set the value of `gui_scale` in `config.txt` to the GUI Scale in Minecraft.

## Use a release
### Linux
1. Unzip
    ```bash
    tar -xvzf autofisher_linux_x64.tar.gz  
    ```
2. Navigate to directory
    ```bash
    cd autofisher
    ```
3. Execute autofisher
    ```bash
    ./autofisher
    ```

### Is it running?
The program is running if the console prints out
```py
Searching screen...
```

### Windows
1. Unzip<br>
    Unzip the `autofisher_win_x64.zip` file
2. Navigate to directory<br>
    Open the directory autofisher
3. Execute autofisher<br>
    Double click on autofisher.exe

## Use source code
### Install Python
Install python 11.6, if not already installed.<br>
If you are on windows check the box `Add python.exe to PATH` in the installer
If you are on Linux make sure to isntall python3-dev
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
4. Start the script
    ``` bash
    python3 main.py
    ```

### Windows
1. Set up a virtual environment (optional but recommend)
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment
    ```bash
    venv\Scripts\activate
    ```
3. Install dependencies
    ```bash
    pip install pyautogui pynput opencv-python
    ```
4. Start the script
    ``` bash
    python main.py
    ```

## Notes
- This script has only been tested on Linux with Debian and KDE Plasma.
- **Caution:** The use of this script may be considered cheating on some servers. Please use it responsibly.
