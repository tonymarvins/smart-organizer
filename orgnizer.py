# organizer.py
# Handles file organization

import os
import shutil
from utils import log_message


def organize_files(files):
    """
    Moves files into categorized folders
    """

    folders = {
        "images": [".jpg", ".png", ".jpeg", ".gif"],
        "code": [".py", ".js", ".html", ".css"],
        "documents": [".pdf", ".txt", ".docx"]
    }

    for file in files:

        # skip folders
        if not os.path.isfile(file):
            continue

        for folder, extensions in folders.items():

            if any(file.lower().endswith(ext) for ext in extensions):

                try:
                    # create folder if it does not exist
                    os.makedirs(folder, exist_ok=True)

                    destination = os.path.join(folder, file)

                    # avoid overwrite if file already exists
                    if os.path.exists(destination):
                        print(f"Skipping {file} (already exists)")
                        log_message(f"Skipped {file}, already exists")
                        break

                    shutil.move(file, destination)

                    print(f"Moved {file} -> {folder}/")
                    log_message(f"Moved {file} to {folder}")

                except Exception as e:
                    print(f"Error moving {file}: {e}")
                    log_message(f"Move error {file}: {e}")

                break
