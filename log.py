import time

def timestamp(func):
    def wrapper(*args, **kwargs):
        current_time = time.ctime()
        print(current_time)
        result = func(*args, **kwargs)
        return result

    return wrapper

