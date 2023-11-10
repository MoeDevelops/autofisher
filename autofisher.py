from pynput.mouse import Button, Controller
import pyautogui
import time

mouse = Controller()

def click():
    mouse.press(Button.right)
    mouse.release(Button.right)

counter = 0

while True:
    time.sleep(0.25)
    try:
        if pyautogui.locateOnScreen(image="resources/Bobber.png", grayscale=True, confidence=0.8) is not None:
            counter += 1
            print("Bobber went down. Counter:", counter)
            click()
            time.sleep(2)
            click()
            time.sleep(5)
    except Exception as e:
        print(f"Couldn't find image {e}")
