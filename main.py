import scanner
from utils import setup_logger, log_message
import sys
auto_organize = "--organize" in sys.argv
if auto_organize:
    import organizer
    organizer.organize_files(".")
    log_message("Files automatically organized via CLI argument")
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

       #keyword search
    keyword = input("\nEnter keyword to search files (or leave empty): ")
    if keyword:
        results = scanner.search_files(files, keyword)
        print("\nSearch results:")
        for r in results:
            print("->", r)
        log_message(f"Search results: {results}")
    organize_choice = input("\nDo you want to organize files into folders by type? (y/n): ")
    if organize_choice.lower() == "y":
    import organizer
    organizer.organize_files(".")
    log_message("Files organized successfully")

    print("\nScan complete. See scan.log for full details.")


if __name__ == "__main__":
    main()
