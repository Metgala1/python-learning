import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debugging message")
logging.info("Application started")
logging.warning("Disk space is getting low")
logging.error("Payment failed")
logging.critical("Database is unavailable")
