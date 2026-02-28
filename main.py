import scanner

def main():
    files = scanner.scan_folder(".")
    print("Scanning current folder...\n")

    for f in files:
        print("Found:", f)

if __name__ == "__main__":
    main()
