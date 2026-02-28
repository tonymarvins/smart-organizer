import scanner
from utils import setup_logger, log_message

def main():
    setup_logger()
    log_message("Smart Scanner started")

    files = scanner.scan_folder(".")
    print("Scanning current folder...\n")

    for f in files:
        print("Found:", f)
        #filter only .py files
    py_files = scanner.filter_by_extension(files, ['.py'])
    print("\nPython files in folder:")
    for f in py_files:
        print("->", f)
        #folder statistics
    count, size = scanner.file_statistics(files)
    print(f"\nTotal files: {count}, Total size: {size} bytes")

    log_message(f"Python files: {py_files}")

   
    keyword = input("\nEnter keyword to search files (or leave empty): ")
    if keyword:
        results = scanner.search_files(files, keyword)
        print("\nSearch results:")
        for r in results:
            print("->", r)
        log_message(f"Search results: {results}")

    print("\nScan complete. See scan.log for full details.")


if __name__ == "__main__":
    main()
