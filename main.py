from modules.logger import log
from modules.configreader import getGuiScale
from modules.io_controller import click, imageIsOnScreen
import time

if __name__ == "__main__":
    counter = 0
    guiScale = getGuiScale()

    while True:
        time.sleep(0.2)
        
        if result := imageIsOnScreen(guiScale) == True:
            counter += 1
            log(f"Bobber went down. Counter: {counter}")
            click()
            time.sleep(2)
            click()
            time.sleep(3)
        else:
            log(f"Searching screen...")

            if result is Exception:
                log(f"ERROR: {result}")