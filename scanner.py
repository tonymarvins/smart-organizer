#handles directory scanning
import os
def scan_folder(path):
    try:
        return os.listdir(path)
    except Exception as e:
        print("Scan error:", e)
         return []
def filter_by_extension(files, extensions):
    """
    Return only files that match given extensions.
    Example: filter_by_extension(['a.txt','b.jpg'], ['.txt']) -> ['a.txt']
    """
    return [f for f in files if any(f.endswith(ext) for ext in extensions)]
