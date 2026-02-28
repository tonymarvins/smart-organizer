import scanner 
def main()
    files = scanner.scan_folder(".")
    print(files)
    for f in files:
        print("Found:", f)
    def scan_folder(path):
        try:
            return os.listdr(path)
        except Exception as e;
            print("Scan error:", e)
            return []
if __name__ == "__main__":
    main()
