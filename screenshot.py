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

'''
folder_path = path
screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
file_path = f"{folder_path}\\{screenshot_name}"

screenshot = take_screenshot()
screenshot.save(file_path)



# Read the content of the screenshot file
with open(file_path, "rb") as file:
    content = file.read()

def read_access_token():
with open('config.txt', 'r') as file:
access_tok = file.read().strip()
return access_tok



# Read the access token from the file
access_token = read_access_token()
print(access_token)

# Initialize GitHub object
g = Github(access_token)
repo = g.get_user().get_repo("pythontest")
print(repo)
'''





'''
def take_screenshot():
screenshot = pyautogui.screenshot()
return screenshot
'''

# while True:

# screenshot details

'''
# Upload the file to the repository
repo.create_file(f"{screenshot_name}", "commit message", content)
# time.sleep(60)
'''
