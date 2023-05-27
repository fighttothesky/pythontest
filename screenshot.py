import pyautogui
from datetime import datetime
import os
from github_helper import GithubHelper
from localdata_dir import create_dir


def take_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

# screenshot details
folder_path = create_dir()
screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
file_path = f"{folder_path}\\{screenshot_name}"

screenshot = take_screenshot()
screenshot.save(file_path)

print("Screenshot captured:", screenshot_name)

# Read the content of the screenshot file
with open(file_path, "rb") as file:
    content = file.read()

# Upload the file to the repository
github_helper = GithubHelper()
github_helper.create_file("pythontest", f"{screenshot_name}", "commit message", content)
