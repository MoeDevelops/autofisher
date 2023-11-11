from pynput.mouse import Button, Controller
import pyautogui

mouse = Controller()

def click():
    mouse.press(Button.right)
    mouse.release(Button.right)

def imageIsOnScreen(guiScale):
    try:
        return pyautogui.locateOnScreen(image=f"resources/Bobber{guiScale}.png", grayscale=True, confidence=0.8) is not None
    except Exception as e:
        return e
