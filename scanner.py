#handles directory scanning
import os
def scan_folder(path):
    files = os.listdir(path)
    return files
