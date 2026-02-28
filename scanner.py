#handles directory scanning
import os
def scan_folder(path):
    try:
        return os.listdr(path)
    except Exception as e;
        print("Scan error:", e)
         return []
