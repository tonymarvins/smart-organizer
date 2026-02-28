#organizer.py
#file organizing logic
#moving files into folders by typr

import os
from utils import log_message

def organize file(path):
    """Stub function for organizing files"""
    log-message("Organizer initialized")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    log_message(f"Found {len(files)} files to organize")
# simple move: create "Documents" folder for .txt files
for f in files:
    if f.endswith(".txt"):
        folder_path = os.path.join(path, "Documents")
        os.makedirs(folder_path, exist_ok=True)
        os.rename(os.path.join(path, f), os.path.join(folder_path, f))
        log_message(f"Moved {f} to Documents")
 # add Images folder
for f in files:
    if f.endswith((".jpg", ".png", ".jpeg")):
        folder_path = os.path.join(path, "Images")
        os.makedirs(folder_path, exist_ok=True)
        os.rename(os.path.join(path, f), os.path.join(folder_path, f))
        log_message(f"Moved {f} to Images")
