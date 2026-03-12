import random
class MaxRetryAttemptsReached(Exception):
    pass
def retry(max_attempts):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args,**kwargs)
                except Exception:
                    if i == max_attempts-1:
                        raise MaxRetryAttemptsReached('Try again after some time')
        return wrapper

    return decorator

@retry(3)
def unreliable():
    if random.random() < 0.7:
        raise ValueError("Failure")
    return "Success"

print(unreliable())