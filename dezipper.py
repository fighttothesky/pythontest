import os
import zipfile
import pyAesCrypt

def extract_zip_with_password(zip_path, extract_path, password):
    # Decrypt the zip file
    decrypted_zip_path = f"{zip_path}.decrypted"
    bufferSize = 64 * 1024
    pyAesCrypt.decryptFile(zip_path, decrypted_zip_path, password, bufferSize)

    # Extract the contents of the decrypted zip file
    with zipfile.ZipFile(decrypted_zip_path, 'r') as zipf:
        zipf.extractall(extract_path)

    # Remove the decrypted zip file
    os.remove(decrypted_zip_path)


# Example usage
zip_path = "C:\\Users\\User\\Desktop\\test.zip"  # Specify the path of the output zip file
extract_path = "C:\\Users\\User\\Desktop\\test2"  # Specify the path where the contents will be extracted
password = "uiopuiop"  # Set the desired password for the zip fil

extract_zip_with_password(zip_path, extract_path, password)
print("Zip file extracted successfully!")
