import scanner 
def main()
    files = scanner.scan_folder(".")
    print(files)
    for f in files:
        print("Found:", f)
if __name__ == "__main__":
    main()
