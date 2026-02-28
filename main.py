import scanner

def main():
    files = scanner.scan_folder(".")
    print("Scanning current folder...\n")

    for f in files:
        print("Found:", f)
        
    # Filter only .py files for now
    py_files = scanner.filter_by_extension(files, ['.py'])
    print("\nPython files in folder:")
    for f in py_files:
    print("->", f)

    count, size = scanner.file_statistics(files)
    print(f"\nTotal files: {count}, Total size: {size} bytes")
if __name__ == "__main__":
    main()
