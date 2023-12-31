import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.5f} seconds to run.")
        return result
    return wrapper

@timer_decorator
def slow_function(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    slow_function(2)
