import platform
from localdata_dir import create_dir
from github_helper import GithubHelper
from datetime import datetime

folder_path = create_dir()


class SystemInfo:

    def __init__(self):
        self.system_info = self.get_system_info()

    def get_system_info(self):
        system_info = {'System': platform.system(), 'Node Name': platform.node(), 'Release': platform.release(),
                       'Version': platform.version(), 'Machine': platform.machine(), 'Processor': platform.processor()}

        return system_info

    # Make a .txt file to push to the repository with the information about the system
    def print_system_info(self):
        with open(f"{folder_path}\\systeminfo.txt", 'a') as file:
            for key, value in self.system_info.items():
                print(key + ':', value)
                file.write(key + ': ' + value + '\n')


if __name__ == '__main__':
    system = SystemInfo()
    system.get_system_info()
    system.print_system_info()
    # Make a .txt file to push to the repository that the zip file was created
    file_path = f"{folder_path}\\systeminfo.txt"
    with open(file_path, 'r') as file:
        content = file.read()

    github_helper = GithubHelper()
    github_helper.create_file("pythontest", f"userinfo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", "zipped",
                              content)
