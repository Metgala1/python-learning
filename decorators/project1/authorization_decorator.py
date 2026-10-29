from functools import wraps
import logging
from logging_decorator import log_operation

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def require_role(required_role):
    def decorator(original_function):
        @wraps(original_function)
        def wrapper(user_role, *args , **kwargs):
            if user_role != required_role:
                logging.warning(
                    "Access denied for role %s on %s",
                    user_role,
                    original_function.__name__,
                )
                raise PermissionError(
                    f"Required role: {required_role}"
                )
            return original_function(user_role , *args , **kwargs)
    
        return wrapper
    return decorator


deletion_attempts = []


@log_operation
@require_role("ADMIN")
def delete_user(user_role, user_id):
    deletion_attempts.append(user_id)
    return True


# Administrator: allowed.
delete_user("ADMIN", 42)

assert deletion_attempts == [42]


# Customer: rejected before deletion logic executes.
try:
    delete_user("CUSTOMER", 99)
except PermissionError:
    pass

assert deletion_attempts == [42]

print("All authorization tests passed!")
  