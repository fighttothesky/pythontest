import pyautogui
from datetime import datetime


class Screenshot:
    def __init__(self):
        self.screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        #screenshot.save(self.path)
        return screenshot

    def take_screenshot_with_time(self):
        screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

        #take_screenshot()

        print("Screenshot captured:", screenshot_name)
