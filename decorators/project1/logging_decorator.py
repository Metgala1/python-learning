import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_operation(original_function):
    @wraps(original_function)
    def wrapper(*args , **kwargs):
        logging.info(f"[LOG] starting: {original_function.__name__}")
        try:
            result = original_function(*args , **kwargs)
        except Exception as error:
           logging.exception(
               "Operation failed: %s",
               original_function.__name__,
           )
           raise
        else:
            logging.info(f"Finished: %s", original_function.__name__)
            return result
    return wrapper

