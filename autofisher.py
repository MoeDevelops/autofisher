from pynput.mouse import Button, Controller
import pyautogui
import time

mouse = Controller()

def log(message: str):
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    print(f"[{timestamp}] {message}")

def click():
    mouse.press(Button.right)
    mouse.release(Button.right)

def readConfig():
    config = {}
    with open("config.txt", "r") as config_file:
        for line in config_file:
            key, value = line.strip().split("=")
            config[key] = value
    return config

def getGuiScale():
    return int(readConfig().get('gui_scale'))

counter = 0
guiScale = getGuiScale()

while True:
    time.sleep(0.2)
    try:
        if pyautogui.locateOnScreen(image=f"resources/Bobber{guiScale}.png", grayscale=True, confidence=0.8) is not None:
            counter += 1
            log("Bobber went down. Counter:", counter)
            click()
            time.sleep(2)
            click()
            time.sleep(3)
    except Exception as e:
        log(f"Bobber isn't down {e}")
