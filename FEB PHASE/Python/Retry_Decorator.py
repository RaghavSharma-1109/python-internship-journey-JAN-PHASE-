import random
from functools import wraps

class MaxRetryAttemptsReached(Exception):
    pass

def retry(max_attempts):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    print(f"Attempt {i+1} failed")

                    if i == max_attempts - 1:
                        raise MaxRetryAttemptsReached(
                            "Max retry attempts reached"
                        ) from e

        return wrapper

    return decorator


@retry(3)
def unreliable():
    if random.random() < 0.7:
        raise ValueError("Failure")
    return "Success"

print(unreliable())