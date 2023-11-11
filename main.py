from modules.logger import log
import modules.config_reader as config
import modules.io_controller as io
import time


if __name__ == "__main__":
    counter = 0
    guiScale = config.get_gui_scale()
    sleep_time = config.get_sleep_between_reads()

    while True:
        time.sleep(sleep_time)

        result = io.image_is_on_screen(guiScale)
        
        if result == True:
            counter += 1
            log(f"Bobber went down. Counter: {counter}")
            io.click()
            time.sleep(2)
            io.click()
            time.sleep(3)
        else:
            log(f"Searching screen...")

            if result is Exception:
                log(f"ERROR: {result}")
