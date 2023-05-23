import pyautogui
from datetime import datetime
import time


def take_screenshot(path):
    screenshot = pyautogui.screenshot()
    screenshot.save(path)


while True:
    folder_path = "C:\\Users\\User\\Desktop\\test"

    screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    file_path = f"{folder_path}\\{screenshot_name}"

    take_screenshot(file_path)

    print("Screenshot captured:", screenshot_name)

    time.sleep(60)