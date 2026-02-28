import logging
def setup_logger():
    logging.basicConfig(
        filename="scan.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_message(msg):
    print("[LOG]", msg)
    logging.info(msg)
