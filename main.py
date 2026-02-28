import scanner
import organizer
from utils import setup_logger, log_message


def main():
    setup_logger()
    log_message("Smart Scanner started")

    print("Scanning current folder...\n")

    files = scanner.scan_folder(".")

    for f in files:
        print("Found:", f)

    # Filter Python files
    py_files = scanner.filter_by_extension(files, ['.py'])

    print("\nPython files:")
    for f in py_files:
        print("->", f)

    # Statistics
    count, size = scanner.file_statistics(files)
    print(f"\nTotal files: {count}")
    print(f"Total size: {size} bytes")

    log_message(f"Python files: {py_files}")

    # Keyword search
    keyword = input("\nEnter keyword to search (or press Enter): ")

    if keyword:
        results = scanner.search_files(files, keyword)

        print("\nSearch results:")
        for r in results:
            print("->", r)

        log_message(f"Search results: {results}")

    print("\nScan complete. Check scan.log.")


if __name__ == "__main__":
    main()
