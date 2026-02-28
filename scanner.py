# handles directory scanning
import os
from utils import log_message

def scan_folder(path):
    try:
        files = os.listdir(path)
        # log each found file
        for f in files:
            log_message(f"Found file: {f}")
        return files
    except Exception as e:
        print("Scan error:", e)
        return []

def filter_by_extension(files, extensions):
    """
    Return only files that match given extensions.
    Example: filter_by_extension(['a.txt','b.jpg'], ['.txt']) -> ['a.txt']
    """
    return [f for f in files if any(f.endswith(ext) for ext in extensions)]

def file_statistics(files):
    """
    Returns number of files and total size in bytes
    """
    total_size = 0
    for f in files:
        if os.path.isfile(f):
            total_size += os.path.getsize(f)
    return len(files), total_size

def search_files(files, keyword):
    """
    Returns files containing the keyword in name
    """
    return [f for f in files if keyword.lower() in f.lower()]
