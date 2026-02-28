import os


def scan_folder(path):
    try:
        return os.listdir(path)
    except Exception as e:
        print("Scan error:", e)
        return []


def filter_by_extension(files, extensions):
    return [f for f in files if any(f.endswith(ext) for ext in extensions)]


def file_statistics(files):
    total_size = 0

    for f in files:
        if os.path.isfile(f):
            total_size += os.path.getsize(f)

    return len(files), total_size


def search_files(files, keyword):
    return [f for f in files if keyword.lower() in f.lower()]
