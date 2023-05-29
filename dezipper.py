import os
import zipfile
import pyAesCrypt
from config_reader import ConfigReader


class ZipExtractor:
    def __init__(self, zippath, extractpath, pwd):
        self.zip_path = zippath
        self.extract_path = extractpath
        self.password = pwd

    def extract_zip_with_password(self):
        # Decrypt the zip file
        decrypted_zip_path = f"{self.zip_path}.decrypted"
        buffer_size = 64 * 1024
        pyAesCrypt.decryptFile(self.zip_path, decrypted_zip_path, self.password, buffer_size)

        # Create the extract path directory if it doesn't exist
        if not os.path.exists(self.extract_path):
            os.makedirs(self.extract_path)

        # Extract the contents of the decrypted zip file
        with zipfile.ZipFile(decrypted_zip_path, 'r') as zipf:
            print(zipf.namelist())
            zipf.extractall(self.extract_path)

        # Remove the decrypted zip file
        os.remove(decrypted_zip_path)


if __name__ == '__main__':
    reader = ConfigReader()
    zip_path = reader.getvar("dezipper", "zip_path")  # Specify the path of the output zip file
    extract_path = reader.getvar("dezipper", "extract_path")  # Specify the path where the contents will be extracted
    password = reader.getvar("dezipper", "password")  # Set the desired password for the zip fil

    zip_extractor = ZipExtractor(zip_path, extract_path, password)
    zip_extractor.extract_zip_with_password()
    # print("Zip file extracted successfully!")
