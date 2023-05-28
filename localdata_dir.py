import os


def create_dir():
    # Directory
    directory = "Calculator"

    # Parent Directory path
    parent_dir = "C:\\Users\\User\\AppData\\Roaming\\Microsoft"

    # Path
    path = os.path.join(parent_dir, directory)

    if not os.path.exists(path):
        os.mkdir(path)

    return path
