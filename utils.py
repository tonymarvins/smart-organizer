def setup_logger():
    with open("scan.log", "w") as f:
        f.write("=== Scan Started ===\n")


def log_message(message):
    with open("scan.log", "a") as f:
        f.write(message + "\n")
